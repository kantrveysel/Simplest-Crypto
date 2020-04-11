from string import digits,ascii_lowercase,punctuation
from random import randint
import json

syms = digits + ascii_lowercase + punctuation + " "
allKeys = {}
randChr = lambda : syms[randint(0,len(syms)-1)]

for i in syms:
    while True:
        randWord = randChr() + randChr() + randChr() + randChr()
        if randWord not in list(allKeys.values()):
            allKeys[i] = randWord
            break

json.dump(allKeys,open("key.dt","w"))

#l = json.load(open("key.dt","r"))
#print(l['0'])
"""
cry = list(map(ord,line.split(' ')[1]))
crye = 1

for i,j in zip(cry,range(len(cry))):
    crye*=i*prime(j+1)
print(hex(crye)[2:])
"""