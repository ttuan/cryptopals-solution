__author__ = 'tuan'

# Be the change you want to see in the world

from Crypto.Cipher import AES
import base64


def AES_in_ECB_mode(key,data):
	mode = AES.MODE_ECB
	decryptor = AES.new(key,mode)
	result = decryptor.decrypt(data)
	return result

if __name__ == '__main__':
	f = open('7.txt','r')
	data = f.read()
	data = base64.b64decode(data)
	key = 'YELLOW SUBMARINE'
	print AES_in_ECB_mode(key,data)