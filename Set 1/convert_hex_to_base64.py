__author__ = 'tuan'

# This is my answer for the challenge at http://cryptopals.com/sets/1/challenges/1/
# It convert hex to base64


import base64


def hexToBase64(s):
    decoded = s.decode("hex")
    return base64.b64encode(decoded)


if __name__ == '__main__':
    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hexToBase64(s)