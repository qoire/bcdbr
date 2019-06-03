import sys

HEADER_PREFIX = b"h"
HEADER_TD_SUFFIX = b"t"
HEADER_HASH_SUFFIX = b"n"
HEADER_NUMBER_PREFIX = b"H"

BLOCK_BODY_PREFIX = b"b"
BLOCK_RECEIPTS_PREFIX = b"r"

TX_LOOKUP_PREFIX = b"l"
BLOOM_BITS_PREFIX = b"B"

def hh_key(bn):
	bnbytes = bn.to_bytes(8, 'big')
	return HEADER_PREFIX + bnbytes + HEADER_HASH_SUFFIX

def bh_key(bn, bh):
	bnbytes = bn.to_bytes(8, 'big')
	return HEADER_PREFIX + bnbytes + bh