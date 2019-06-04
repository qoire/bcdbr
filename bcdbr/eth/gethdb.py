import sys
import plyvel
from pprint import pprint
from rlp import decode

from bcdbr.eth import decoding, types

HEADER_PREFIX = b"h"
HEADER_TD_SUFFIX = b"t"
HEADER_HASH_SUFFIX = b"n"
HEADER_NUMBER_PREFIX = b"H"

BLOCK_BODY_PREFIX = b"b"
BLOCK_RECEIPTS_PREFIX = b"r"

TX_LOOKUP_PREFIX = b"l"
BLOOM_BITS_PREFIX = b"B"

EMPTY_UNCLE_HASH = bytes.fromhex("1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347")
EMPTY_TX_ROOT_HASH = bytes.fromhex("56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421")

def create_db(db_path):
	return plyvel.DB(db_path)

def header_hash_key(block_num):
	bnbytes = block_num.to_bytes(8, 'big')
	return HEADER_PREFIX + bnbytes + HEADER_HASH_SUFFIX

def block_header_key(block_num, block_hash):
	bnbytes = block_num.to_bytes(8, 'big')
	return HEADER_PREFIX + bnbytes + block_hash

def block_body_key(block_num, block_hash):
	return BLOCK_BODY_PREFIX + block_num.to_bytes(8, 'big') + block_hash

def block_receipts_key(block_num, block_hash):
	return BLOCK_RECEIPTS_PREFIX + block_num.to_bytes(8, 'big') + block_hash

# debug functionality for tests, dont use for prod
def get_block_body(db, block_num):
	block_hash = db.get(header_hash_key(block_num))

	if not block_hash:
		return None

	return db.get(block_body_key(block_num, block_hash))

def get_receipts(db, block_num):
	block_hash = db.get(header_hash_key(block_num))

	if not block_hash:
		return None

	return db.get(block_receipts_key(block_num, block_hash))

def get_fullblock_from_num(db, block_num, drop_uncles=True):
	hh_key = header_hash_key(block_num)
	block_hash = db.get(hh_key)

	if not block_hash:
		return None

	header_bytes = db.get(block_header_key(block_num, block_hash))
	block_header = decoding.block_header(header_bytes)

	# optimization: no need to retrieve empties
	if (block_header.transactionsroot == EMPTY_TX_ROOT_HASH and
		(drop_uncles or (block_header.uncleshash == EMPTY_UNCLE_HASH))):
		return types.make_block(block_header, [], [])

	# otherwise, need to retrieve body
	body_bytes = db.get(block_body_key(block_num, block_hash))
	body = decoding.block_body(body_bytes)
	uncles = [] if drop_uncles else body.uncles

	if (block_header.transactionsroot == EMPTY_TX_ROOT_HASH):
		return types.make_block(block_header, body.transactions, uncles)

	receipt_bytes = db.get(block_receipts_key(block_num, block_hash))
	receipts = decoding.receipts(receipt_bytes)

	return types.make_block(block_header, body.transactions, uncles, receipts)
