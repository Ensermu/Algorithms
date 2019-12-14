import math
def karatsuba(a, b):
    if len(a) == 1 and len(b) == 1:
        return int(a) * int(b)
    if len(a) > len(b):
        dif = len(a) - len(b)
        b = dif * '0' + b
    if len(b) > len(a):
        dif = len(b) - len(a)
        a = dif * '0' + a
    x1 = a[0 : math.ceil(len(a)/2)]
    x0 = a[math.ceil(len(a)/2) : len(a)+1]
    y1 = b[0 : math.ceil(len(b)/2)]
    y0 = b[math.ceil(len(b)/2) : len(b)+1]
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1) 
    x = str(int(x0) + int(x1))
    y = str(int(y0) + int(y1))
    z1 = karatsuba(x, y) - z0 - z2
    z = z2 * (10**len(a)) + z1*(10**(len(a)//2)) + z0
    return z
