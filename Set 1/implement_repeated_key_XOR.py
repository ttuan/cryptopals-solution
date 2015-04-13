__author__ = 'tuan'

# Be the change you want to see in the world

from Crypto.Util.strxor import strxor


def find_repeated_key(key, length):
    repeatedKey = ""
    count = 0
    while count < length:
        repeatedKey += key[count % len(key)]
        count += 1
    return repeatedKey


key = "ICE"
s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
re_key = find_repeated_key(key,len(s))

result = strxor(s,re_key).encode("hex")
print result




