# Kelompol 1

from Crypto.Util.number import long_to_bytes

e = 3
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

def rt(l, n):
    a = n 
    b = n + 1
    while a < b:
        b = a
        c = (l - 1) * b + (n // pow(b, l - 1))
        a = c // l
    return a

print(long_to_bytes(rt(e, ct)).decode())

# flag = crypto{N33d_m04R_p4dd1ng}