from Crypto.Util.number import inverse
num1 = 857504083339712752489993810777
num2 = 1029224947942998075080348647219
num3 = 65537

phi = (num1 - 1) * (num2 - 1)

num4 = inverse(num3, phi)

print(num4)