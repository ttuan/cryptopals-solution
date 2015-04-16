__author__ = 'tuan'

# Be the change you want to see in the world


def pad(s, block_size):
	y = s
	while len(y) % block_size:
		y += '\x04'
	return y

if __name__ == '__main__':
	s = "YELLOW SUBMARINE"
	print pad(s,20)