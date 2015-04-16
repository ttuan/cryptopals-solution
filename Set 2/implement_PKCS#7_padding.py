__author__ = 'tuan'

# Be the change you want to see in the world

def pad(s, pad_len):
	y = s
	for i in range(len(s),pad_len):
		y += '\x04'
	return y

if __name__ == '__main__':
	s = "YELLOW SUBMARINE"
	print pad(s,20)
