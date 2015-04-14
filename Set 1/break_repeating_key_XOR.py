__author__ = 'tuan'

# be the chance you want to see in the world
# this is solution for challenge 6 in http://cryptopals.com/sets/1/challenges/6/
# this is really interesting ^^


import distance
import base64
import itertools
import single_byte_XOR_cipher
import implement_repeated_key_XOR


def hamming_distance(a,b):
	aBin = ' '.join(format(ord(x),'08b') for x in a)
	bBin = ' '.join(format(ord(x),'08b') for x in b)
	return distance.hamming(aBin,bBin)


def average_hamming_distance(data,k):
	chunks = [data[i: i+k] for i in range(0,len(data),k)][0:20]
	score = 0
	for i in range(20):
		score += hamming_distance(chunks[0], chunks[i])/float(k)
	return score/20


def find_key(data,key_size):
	blocks = [data[i: i+key_size] for i in range(0,len(data),key_size)]
	transposedBlocks = list(itertools.izip_longest(*blocks,fillvalue='0'))
	key = ''
	for x in transposedBlocks:
		s = ''.join(x)
		key += chr(single_byte_XOR_cipher.find_key(s))
	return key


if __name__ == '__main__':
	f = open("6.txt", "r")
	data = f.read()
	data = base64.b64decode(data)

	key_size = min(range(2,41), key = lambda k: average_hamming_distance(data,k))
	key = find_key(data,key_size)

	result = implement_repeated_key_XOR.solve(key,data)
	print result.decode("hex")
