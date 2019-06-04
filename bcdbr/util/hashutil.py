from Crypto.Hash import keccak

def keccak256(in: bytes) -> bytes:
	h: bytes = keccak.new(digest_bits=256)
	h.update(in)
	return h.digest()
