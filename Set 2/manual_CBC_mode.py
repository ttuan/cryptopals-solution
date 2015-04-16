__author__ = 'tuan'

# Be the change you want to see in the world
# See more about block cipher mode in here : http://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

import base64
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

class CBC:
	def __init__(self, ECB, iv):
		self._ECB = ECB
		self._iv = iv
		self._block_size = 16

	def get_blocks(self,text):
		return [text[i: i + self._block_size] for i in range(0, len(text), self._block_size)]

	def decrypt(self, text):
		plain_text = ''
		cipher_blocks = self.get_blocks(text)
		previous = self._iv
		for block in cipher_blocks:
			plain_text += strxor(self._ECB.decrypt(block), previous)
			previous = block
		return plain_text


if __name__ == '__main__':
	data = base64.b64decode(open('10.txt','r').read())
	iv = '\x00' * 16
	key = 'YELLOW SUBMARINE'
	cipher = CBC(AES.new(key,AES.MODE_ECB),iv)

	print cipher.decrypt(data)