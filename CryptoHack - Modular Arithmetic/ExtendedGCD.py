def extendedGCD(a, y):
    if(a==0):
        return y,0,1

    gcd,x1,y1 = extendedGCD(y%a, a)

    x = y1 - (y//a) * x1
    y = x1

    return gcd,x,y

a = 26513
b = 32321
g, u, v = extendedGCD(a, b)

print("{%d,%d}" % (u, v))