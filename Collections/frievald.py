import random

def frievald(A, B, C):
    r = []
    for i in range(len(A)):
        r.append(random.randint(0, 1))
    b = multiply(B, r)
    a = multiply(A, b)
    c = multiply(C, r)
    return a == c

def multiply(a, b):
    x = [0]*len(b)
    for i in range(len(a)):
        for j in range(len(a)):
            x[i] += a[i][j]*b[j]
    return x

A = [[2, 3], 
     [3, 4]]
B = [[1, 0],
     [1, 2]]
C = [[6, 5],
     [8, 7]]
     
print(frievald(A, B, C))