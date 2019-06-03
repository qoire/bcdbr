from rlp import decode

def block_header(b):
	l = decode(b)
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