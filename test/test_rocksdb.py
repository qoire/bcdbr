import rocksdb
import plyvel
from rlp import decode
from pprint import pprint
import decoding

GETH_DB_PATH = "/home/yao/Ethereum/geth-linux-amd64-1.8.27-4bcc0a37/geth-storage/geth/chaindata"

HEADER_PREFIX = b"h"
HEADER_TD_SUFFIX = b"t"
HEADER_HASH_SUFFIX = b"n"
HEADER_NUMBER_PREFIX = b"H"

BLOCK_BODY_PREFIX = b"b"
BLOCK_RECEIPTS_PREFIX = b"r"

TX_LOOKUP_PREFIX = b"l"
BLOOM_BITS_PREFIX = b"B"

def hhash_key(block_number):
    bnbytes = block_number.to_bytes(8, 'big')
    return HEADER_PREFIX + bnbytes + HEADER_HASH_SUFFIX

def bh_key(bn, bh):
    bnbytes = bn.to_bytes(8, 'big')
    return HEADER_PREFIX + bnbytes + bh

def test_gethdb_block_rlp():
    db = plyvel.DB(GETH_DB_PATH)
    block_hash = db.get(hhash_key(1024))
    block_header = db.get(bh_key(1024, block_hash))
    pprint(decoding.block_header(block_header))