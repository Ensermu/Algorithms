import math
def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1
    return A

def radix_sort(A):
    n = len(A)
    u = 1 + max([x for x in A])
    d = math.ceil(math.log(u, n))
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i]
        for j in range(d):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(d):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
    return A
