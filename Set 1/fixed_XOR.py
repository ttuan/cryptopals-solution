__author__ = 'tuan'


from Crypto.Util.strxor import strxor

encodedL = '1c0111001f010100061a024b53535009181c'
encodedR = '686974207468652062756c6c277320657965'

s = encodedL.decode("hex")
t = encodedR.decode("hex")

result = strxor(s, t).encode("hex")
print result