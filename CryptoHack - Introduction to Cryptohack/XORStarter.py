#Soal XOR Starter

inistring = "label"
flag = ""

for i in inistring:
    flag += chr(ord(i)^13)

print(flag)