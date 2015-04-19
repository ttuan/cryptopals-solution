__author__ = 'tuan'

# Be the change you want to see in the world
# This is my solution for challenge at http://cryptopals.com/sets/2/challenges/12/


import base64
from Crypto.Cipher import AES
import random


def pad(text):
	while len(text) % 16:
		text += '\x00'
	return text


def rand_key(len_key):
	randkey = ''
	for i in range(len_key):
		randkey += chr(random.randint(0, 255))
	return randkey

key = rand_key(16)                          # we make a random key, but length 16 is secret


# this function like AES-128-ECB(your string || unknown string, random key) ---> you give a string, it append an unknown
# string and encrypt them with an unknown random key. Our mission is finding what is 'unknown string'
def oracle(s):
	smt = ''' Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
		aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
		dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
		YnkK'''
	plain_text = s + base64.b64decode(smt)
	crypto = AES.new(key, AES.MODE_ECB)
	return crypto.encrypt(pad(plain_text))


def find_block_size():
	"""
		Feed identical bytes of your-string to the function 1 at a time ---
		start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the block size of the cipher.
	"""
	for i in range(1, 100):
		s = 'A'*i*2
		enc_oracle = oracle(s)
		if enc_oracle[:i] == enc_oracle[i: 2*i]:
			return i
	return None


def confirm_ECB(block_size):
	""" Detect that the function is using ECB. """
	s = 'A' * 2 * block_size
	cipher_text = oracle(s)
	if cipher_text[:block_size] == cipher_text[block_size:2*block_size]:
		print "This is using ECB mode"

	else:
		print "It is not using ECB mode"


def find_next_char(block_size, known_string):
	s = 'A' * (block_size - (len(known_string) % block_size) - 1)
	d = {}
	for i in range(256):
		enc = oracle(s + known_string + chr(i))[:len(s) + len(known_string) + 1]
		d[enc] = chr(i)
	c = oracle(s)[:len(s) + len(known_string) + 1]
	if c in d:
		return d[c]
	return None


if __name__ == '__main__':
	block_size = find_block_size()
	confirm_ECB(block_size)
	known_string = ''
	c = ''
	while c is not None:
		known_string += str(c)
		c = find_next_char(block_size, known_string)
	print known_string


# def main():
# 	found = ''
# 	block_size = 128
#
# 	for i in range(block_size -1 , 0, -1):
# 		input_block = 'A' * i
# 		d = {}
# 		for j in range(256):
# 			enc = oracle(input_block + found + chr(j))[:block_size]
# 			d[enc] = chr(j)
# 		found += d[oracle(input_block)[:block_size]]
# 	print found
#
#
#
#
# def find_next_byte(block_size):
# 	"""
# 		if our unknown string is "HELLO WORLD" and block size is 8, we create a input block 'AAAAAAA'
# 		so that by crafting a plaintext that will be 7 bytes, the 8th byte will be H ('AAAAAAAH').
# 	"""
# 	input_block = 'A'*(block_size-1)
# 	d = {}
# 	# make a dictionary with keys are encrypt of (input block and a char i), store it with value i
# 	for i in range(256):
# 		enc = oracle(input_block+chr(i))[:block_size]
# 		d[enc] = i
# 	# oracle(s)[:block size] with s is 'AAAAAAA' will return ecrypted text of 'AAAAAAAH', so we will find
# 	# first char in Unknown key is 'H'
# 	return chr(d[oracle(input_block)[:block_size]])