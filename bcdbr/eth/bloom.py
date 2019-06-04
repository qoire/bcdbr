from bcdbr.util import keccak256

HEADER_BYTES = 6
def verify_bloom(in: bytes, bloom: bytes) -> bytes:
	bloom: int = int.from_bytes(bloom, "big")
	i: int = 0
	while (i < HEADER_BYTES):
		high: int = in[i] & 0xFF
		i = i + 1
		low: int = in[i] & 0xFF
		i = i + 1
		bloom_bit: int = 1 << ((low + (high << 8)) & 2047)

		if (bloom & bloom_bit == 0):
			return False
	return True

def bloom_has_address(address: bytes, bloom: bytes) -> bytes:
	addrHash: bytes = keccak256(address)
	return verify(addrHash, bloom)

def bloom_has_event(event: bytes, bloom: bytes) -> bytes:
	eventHash: bytes = keccak256(keccak256(event))
	return verify(eventHash, bloom)
