__author__ = 'tuan'

# This is solution for challenge 2 in http://cryptopals.com/sets/1/challenges/2/

from Crypto.Util.strxor import strxor


def fixed_xor(a,b):
	s = a.decode("hex")
	t = b.decode("hex")
	return strxor(s,t).encode("hex")


if __name__ == '__main__':
	a = '1c0111001f010100061a024b53535009181c'
	b = '686974207468652062756c6c277320657965'
	print fixed_xor(a,b)
