# coding=utf-8
__author__ = 'tuan'

# Be the change you want to see in the world

from Crypto.Cipher import AES
import os


rand_key = os.urandom(16)
iv = os.urandom(16)
prepend_string = "comment1=cooking%20MCs;userdata="
append_string = ";comment2=%20like%20a%20pound%20of%20bacon"


def pad(s, block_size):
	pad_len = block_size
	if len(s) % block_size:
		pad_len = block_size - len(s) % block_size
	return s + pad_len * chr(pad_len)


def unpad(s):
	i = s.count(s[-1])
	return s[0: len(s) - i]

def encrypt_input_strings(s):
	s = s.replace("=", "").replace(";", "")
	s = prepend_string + s + append_string
	s = pad(s, 16)
	enc = AES.new(rand_key, AES.MODE_CBC, iv)
	ciphertext = enc.encrypt(pad(s, 16))
	return ciphertext


def decrypt_ciphertext(ciphertext):
	dec = AES.new(rand_key, AES.MODE_CBC, iv)
	plain_text = unpad(dec.decrypt(ciphertext))
	return plain_text.find(';admin=true;') != -1
	# or return ';admin=true;' in plain_text


"""
	Fistly, you must read how to CBC decryption work at http://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
	----------------------------------------------------------------------------
	We need to craft userdata such that it contains ;admin=true' - but we can't use ; or =.
	What we'll do is send some input like :admin@true’ and flip bits on the cyphertext until,
	when decrypting, : becomes ; and @ becomes =
	-----------------------------------------------------------------------------
	000000000000000000000:admin@true
	0123456789ABCDEF0123456789ABCDEF
	-----> You see, ':' is the 5th byte and '@' is the 11

	with CBC decrypt, we have : Pi = C(i-1) XOR D(Ci) ---> P: plain text, C : cipher text, D : decrypt with key.
	so with 2 plain block, we have:
		P2 = C1 ^ D(C2)
	we call P2' is the fake plain text, which contain ';admin=true;', it will replace P2 in plain text
		P2' = P2' ^ P2 ^ C1 ^ D(C2) --------- because of ( A = B --> A ^ B = 1)
		we don't know D(C2) because we don't have key, but we have C1
		if we fake C1' = P2' ^ P2 ^ C1 so P2' = C1' ^ D(C2)

	WE HAVE : P2, C1, P2'. So equation :
					C1' = P2' ^ P2 ^ C1
	is all which we need.
"""


if __name__ == '__main__':
	u = '000000000000000000000:admin@true'  # 32 bytes

	e = bytearray(encrypt_input_strings(u))
	f_pos1 = 32 + 5            # why 32 and 5 : 32 because of prepend_string have 32 bytes, so 32 first bytes
	f_pos2 = 32 + 11           # in e will save encrypt of prepend_string, 5 is the position of fake byte in block 3rd
								# we want to change ';' character in plain text

	# C1' = P2' ^ P2 ^ C1
	e[f_pos1] = ord(';') ^ ord(':') ^ e[f_pos1]                    # change ':' to ';'
	e[f_pos2] = ord('@') ^ ord('=') ^ e[f_pos2]


	print decrypt_ciphertext(bytes(e))