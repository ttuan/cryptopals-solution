__author__ = 'tuan'

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

ss = s.decode("hex")

for key in range(ord('A'),ord('z')+1):
    res = ""
    for cc in ss:
        i = ord(cc) ^ key
        if ord('A') <= i <= ord('z'):
            res += chr(i)
    print res


# CookingMCs like a pound of bacon