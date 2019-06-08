from Crypto.Hash import keccak

def keccak256(i: bytes) -> bytes:
	h: bytes = keccak.new(digest_bits=256)
	h.update(i)
	return h.digest()
