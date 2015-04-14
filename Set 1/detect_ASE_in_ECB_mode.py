__author__ = 'tuan'

# Be the change you want to see in the world
# This is solution for challenge 8 in http://cryptopals.com/sets/1/challenges/8/

import collections


def find_same_block(line):
	block_size = 16

	blocks = [line[i: i + block_size] for i in range(0,len(line),block_size)]
	count = collections.Counter(blocks)

	return count.most_common()[0][1]


if __name__ == '__main__':
	with open('8.txt', 'r') as f:
		lines = f.readlines()
	index = 1
	for line in lines:
		if find_same_block(line) > 1:
			print index
		index += 1
