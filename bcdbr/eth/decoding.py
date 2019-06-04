from rlp import decode
from pprint import pprint
from bcdbr.eth.types import BlockHeader, BlockBody, Log, Transaction, Receipt

def decode_block_header(l):
	return BlockHeader(l[0], l[1], l[2], l[3], l[4], l[5], l[6],
		int.from_bytes(l[7], 'big'), int.from_bytes(l[9], 'big'),
		int.from_bytes(l[10], 'big'), int.from_bytes(l[11], 'big'), l[12])

def block_header(b: bytes) -> BlockHeader:
	l = decode(b)
	return decode_block_header(l)

def block_body(b: bytes) -> BlockBody:
	l = decode(b)
	txs_bytes = l[0]
	uncles_bytes = l[1]

	# presuming this is the only place that decodes these two items
	txs = list(map(decode_transaction, txs_bytes))

	# TODO: figure out uncle decoding
	#uncles = list(map(decode_block_header, txs_bytes))
	return BlockBody(txs, [])

def decode_transaction(l) -> Transaction:
	return Transaction(int.from_bytes(l[0], 'big'), int.from_bytes(l[1], 'big'),
			int.from_bytes(l[2], 'big'), l[3], int.from_bytes(l[4], 'big'),
			l[5], l[6], l[7], l[8])

def receipts(b: bytes) -> Receipt:
	l = decode(b)
	return list(map(decode_receipt, l))

def decode_receipt(l) -> Receipt:
	return Receipt(l[0], int.from_bytes(l[1], 'big'), l[2], l[3], l[4],
		list(map(decode_log, l[5])), int.from_bytes(l[6], 'big'))

def decode_log(l) -> Log:
	return Log(l[0], l[1], l[2])
