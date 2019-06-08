from bcdbr.util.hashutil import keccak256

HEADER_BYTES = 6
def verify_bloom(input: bytes, bloom: bytes) -> bytes:
	bloom: int = int.from_bytes(bloom, "big")
	i: int = 0
	while (i < HEADER_BYTES):
		high: int = input[i] & 0xFF
		i = i + 1
		low: int = input[i] & 0xFF
		i = i + 1
		bloom_bit: int = 1 << ((low + (high << 8)) & 2047)

		if (bloom & bloom_bit == 0):
			return False
	return True

def has_address(address: bytes, bloom: bytes) -> bytes:
	addrHash: bytes = keccak256(address)
	return verify_bloom(addrHash, bloom)

def has_event(event: bytes, bloom: bytes) -> bytes:
	eventHash: bytes = keccak256(keccak256(event))
	return verify_bloom(eventHash, bloom)
