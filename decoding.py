from rlp import decode
from pprint import pprint

def decode_block_header(l):
	return {
		'parenthash': l[0],
		'uncleshash': l[1],
		'author': l[2],
		'stateroot': l[3],
		'transactionsroot': l[4],
		'receiptsroot': l[5],
		'logsbloom': l[6],
		'difficulty': int.from_bytes(l[7], 'big'),
		'number': int.from_bytes(l[8], 'big'),
		'gaslimit': int.from_bytes(l[9], 'big'),
		'gasused': int.from_bytes(l[10], 'big'),
		'timestamp': int.from_bytes(l[11], 'big'),
		'extradata': l[12]
	}

def block_header(b):
	l = decode(b)
	return decode_block_header(l)

def block_body(b):
	l = decode(b)
	txs_bytes = l[0]
	uncles_bytes = l[1]

	# presuming this is the only place that decodes these two items
	txs = list(map(decode_transaction, txs_bytes))

	# TODO: figure out uncle decoding
	#uncles = list(map(decode_block_header, txs_bytes))

	return {
		'transactions': txs,
		'uncles': []
	}

def decode_transaction(l):
	return {
		'accountnonce': int.from_bytes(l[0], 'big'),
		'gasprice': int.from_bytes(l[1], 'big'),
		'gaslimit': int.from_bytes(l[2], 'big'),
		'recipient': l[3],
		'amount': int.from_bytes(l[4], 'big'),
		'payload': l[5],
		'v': l[6],
		'r': l[7],
		's': l[8]
	}

def receipts(b):
	l = decode(b)
	return list(map(decode_receipt, l))

def decode_receipt(l):
	return {
		'posttxstate': l[0],
		'cumulativegas': int.from_bytes(l[1], 'big'),
		'bloom': l[2],
		'txhash': l[3],
		'contractaddress': l[4],
		'logs': list(map(decode_log, l[5])),
		'gasused': int.from_bytes(l[6], 'big')
	}

def decode_log(l):
	return {
		'address': l[0],
		'topics': l[1],
		'data': l[2]
	}
