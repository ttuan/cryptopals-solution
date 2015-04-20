__author__ = 'tuan'

# Be the change you want to see in the world


def pad(s, block_size):
	pad_len = len(s) - len(s) % block_size
	y = s + pad_len * chr(pad_len)
	return y

if __name__ == '__main__':
	s = "YELLOW SUBMARINE"
	print pad(s,20)