from string import digits,ascii_lowercase,punctuation
import json

syms = digits + ascii_lowercase + punctuation + " "

key = json.load(open("key.dt","r"))
newtext = ""
with open("text.txt","r+") as file:
    allfile = file.read().lower()
    for i in allfile:
        if i not in syms:
            allfile = allfile.replace(i,"</br>")
    for i in allfile:
        newtext += key[i]
with open("text.txt","w") as file:
    file.write(newtext)