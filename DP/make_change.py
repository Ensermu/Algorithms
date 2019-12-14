b = {}
parent = {}
def makeChange(n, L):
    if n in b:
        return b[n]
    if n < 0:
        return float('inf')
    if n == 0:
        return 0
    result = float('inf')
    for i in range(1, len(L)+1):
        new = 1 + makeChange(n - L[i-1], L)
        if new < result:
            result = new
            parent[n] = L[i-1]
    b[n] = result
    return result
    
def print_optimal_way(i):
    way = []
    if i not in parent:
        return None
    while True:
        way.append(parent[i])
        if parent[i] == i:
            break
        i = i - parent[i]
    return way

