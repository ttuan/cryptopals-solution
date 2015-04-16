__author__ = 'tuan'

# Be the change you want to see in the world

from Crypto.Cipher import AES
import base64


def AES_in_CBC_mode(key, iv, data):
	mode = AES.MODE_CBC
	decrytor = AES.new(key, mode, iv)
	result = decrytor.decrypt(data)
	return result

if __name__ == '__main__':
	data = base64.b64decode(open('10.txt','r').read())
	iv = '\x00' * 16
	key = 'YELLOW SUBMARINE'

	print AES_in_CBC_mode(key, iv, data)