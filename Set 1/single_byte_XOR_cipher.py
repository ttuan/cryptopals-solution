__author__ = 'tuan'

# This is my answer for the challenge at http://cryptopals.com/sets/1/challenges/3/

import string
from Crypto.Util.strxor import strxor_c

# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def find_score(s):
    score = 0
    for i in s:
        if i in freqs.keys():
            score += freqs[i]
    return score


def solve(h):
    hh = h.decode("hex")

    score_list = dict()
    for k in range(0, 256):
        score_list.update({k : find_score(strxor_c(hh,k))})

    key = max(score_list, key=score_list.get)
    return strxor_c(hh, key)


if __name__ == '__main__':
    h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print solve(h)
