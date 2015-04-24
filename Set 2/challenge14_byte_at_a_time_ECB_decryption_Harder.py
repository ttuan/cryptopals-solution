__author__ = 'tuan'

# Be the change you want to see in the world

import base64
from Crypto.Cipher import AES
import os
import random


def pad(s, block_size):
	pad_len = block_size
	if len(s) % block_size:
		pad_len = block_size - len(s) % block_size
	return s + pad_len * chr(pad_len)


key = os.urandom(16)
# random generate a prefix which has length in range(16,32)- We don't know exactly but we can find it
prefix = os.urandom(random.randint(16,32))

# AES-128-ECB(random-prefix || attacker-controlled || target-bytes, random-key)
def oracle(s):
	smt = ''' Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
		aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
		dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
		YnkK'''
	plain_text = prefix + s + base64.b64decode(smt)
	crypto = AES.new(key, AES.MODE_ECB)
	return crypto.encrypt(pad(plain_text, 16))


def find_prefix_len():
	"""
		Now we will find prefix len. Again it using ECB mode so we can send a block of repeating string
		with length in 32 to 48, we can see duplicate block somewhere
		Assume prefix length is 20

		<--16 bytes prefix--> <--4 bytes prefix + 12 byte--> <--16 bytes--> <---16 byte--> <---target byte-->
		<-------------------20 byte prefix-----> <---------attacked controlled------------>

		So if we see 2 near block are same ( like 3th block and 4th block in this example) , we will find the
		prefix size is 16 * 4 - 44 = 20

	"""
	for i in range(32, 48):
		attack_control = 'A' * i
		enc = oracle(attack_control)

		num_blocks = len(enc) / 16
		for j in range(1, num_blocks):
			if enc[j * 16: (j+1) * 16] == enc[(j + 1) * 16: (j+2)*16]:
				prefix_len = (j + 2) * 16 - i
				return prefix_len
	return None

# Now we do it like challenge 12, but we need to add position of prefix length
def find_next_char(block_size, prefix_len, known_string):
	k1 = block_size - prefix_len % block_size
	k2 = block_size - len(known_string) % block_size - 1
	k3 = prefix_len - prefix_len % block_size
	# now, we need append a string with length = k1 + k2. In challenge 12, length is k2.
	"""
		<----prefix----><-------input-----><--known string-->
		<------make an integer block like 2,3,4,.. block---->
	"""
	s = 'A' * (k1 + k2)
	d = {}
	for i in range(256):
		enc = oracle(s + known_string + chr(i))[k3 + k1 :k3 + len(s) + len(known_string) + 1]
		d[enc] = chr(i)

	c = oracle(s)[k3 + k1: k3 + len(s) + len(known_string) + 1]
	if c in d:
		return d[c]
	return None


if __name__ == '__main__':
	prefix_len = find_prefix_len()
	known_string = ''
	c = ''
	while c is not None:
		known_string += str(c)
		c = find_next_char(16, prefix_len, known_string)
	print known_string
