__author__ = 'tuan'

# This is solution for challenge 4 in http://cryptopals.com/sets/1/challenges/4/

import single_byte_XOR_cipher


def main():
    with open('4.txt','r+') as f:
        lines = f.read().splitlines()

    decodedLines = list()

    for line in lines:
        decodedLines.append(single_byte_XOR_cipher.solve(line))

    def score(i):
        return single_byte_XOR_cipher.find_score(decodedLines[i])

    maxi = max(range(len(decodedLines)),key = score)

    print decodedLines[maxi]


if __name__ == '__main__':
    main()
