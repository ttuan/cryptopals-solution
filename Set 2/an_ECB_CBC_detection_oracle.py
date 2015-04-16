__author__ = 'tuan'

# Be the change you want to see in the world
# This is my solution for challenge in http://cryptopals.com/sets/2/challenges/11/

import random
from Crypto.Cipher import AES


def rand_text(len_key):
	key = ''
	for i in range(len_key):
		key += chr(random.randint(0, 255))
	return key


def encryption_oracle(input_text):
	plain_text = rand_text(random.randint(5, 10)) + input_text + rand_text(random.randint(5, 10))
	log = ''

	key = rand_text(16)
	log += "Encrypt with key: " + key

	rand_mode = random.randint(0, 1)
	if rand_mode == 0:
		encryptor = AES.new(key, AES.MODE_ECB)
		log += ", Mode : ECB "
	else:
		encryptor = AES.new(key, AES.MODE_CBC, rand_text(16))
		log += ", Mode : CBC "

	while len(plain_text) % 16:
		plain_text += '\x00'
	log += "Result: " + encryptor.decrypt(plain_text)
	print log

if __name__ == '__main__':
	encryption_oracle('abcdef')