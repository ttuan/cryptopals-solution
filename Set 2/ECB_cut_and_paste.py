__author__ = 'tuan'

# Be the change you want to see in the world
# This is solution for challenge 13 at http://cryptopals.com/sets/2/challenges/13/
from Crypto.Cipher import AES
from Crypto import Random
import os


def profile_for(s):
	s = s.replace("&", "").replace("=", "")
	d = {'email': s, 'uid': 10, 'role': 'user'}
	return '&'.join('%s=%s' % (k, d[k]) for k in ['email', 'uid', 'role'])


def pad(s, block_size):
	needappend = block_size - len(s) % block_size
	return s + '\x00' * needappend


def unpad(s):
	i = s.count(s[-1])
	return s[0: len(s) - i]


key = os.urandom(16)


def encrypt_email(email):
	enc = AES.new(key, AES.MODE_ECB)
	cipher_text = enc.encrypt(pad(profile_for(email), 16))
	return cipher_text

def decrypt_profile(cipherProfile):
	dec = AES.new(key, AES.MODE_ECB)
	encodedProfile = unpad(dec.decrypt(cipherProfile))
	d = {}
	for pair in encodedProfile.split('&'):
		k, v = pair.split('=')
		d[k] = v
	return d

"""
	Normally, your profile will be divided to many 16 byte blocks
	|email=abc@gmail.|com&uid=10&role=|user............|
	 <--16 bytes----> <----16 bytes--><---16 bytes---->

	Because we don't know what key in ECB mode is, and we only provide email to system, so we will add "admin" word to email
	after that, we cut 16 byte contains "admin" word in cipher text
	Because we lost 6 bytes to store "email=", so we  have 10 bytes to write email before add "admin\x0b...." to email.

	|email=abc@gmail.|admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b|com&uid=10&role=|user............|
	 <--16 bytes----> <----------------16 bytes------------------------><--16 bytes----><--16 bytes---->

	After we have "admin block", we append it to block contain "role=" to being admin : "role=admin"
"""
if __name__ == '__main__':
	enc = encrypt_email('abc@gmail.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bcom')
	ad_block = enc[16: 32]
	c = enc[0:16] + enc[32: 48] + ad_block
	print decrypt_profile(c)
