__author__ = 'tuan'

# Be the change you want to see in the world

def check_validation_of_PKCS7(s, block_size):
	pad_char = s[-1]
	pad_len = s.count(pad_char)
	if len(s) % block_size != 0 or s[len(s) - pad_len:len(s)] != ord(pad_char) * pad_char:
		raise ValueError("Not validation")
	return s[: len(s) - pad_len]

if __name__ == '__main__':
	print check_validation_of_PKCS7("ICE ICE BABY\x04\x04\x04\x04", 16)
	print check_validation_of_PKCS7("ICE ICE BABY\x05\x05\x05\x05", 16)