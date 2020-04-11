from string import digits,ascii_lowercase,punctuation
import json

syms = digits + ascii_lowercase + punctuation + " "

key = json.load(open("key.dt","r"))
ikey = {v:k for k,v in key.items()}
chrs = []
text = ""

with open("text.txt","r+") as file:
    allfile = file.read()
    for i,j in zip(allfile,range(len(allfile))):
        if j%4==0 and j!=0:
            chrs.append(allfile[j-4:j])
    for i in chrs:
        try:
            text += ikey[i]
        except:
            text += "<!!!>"
with open("text.txt","w") as file:
    file.write(text)
