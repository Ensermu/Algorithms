b = {}
def knapsack(L):
    b[(0,0)] = True
    for i in range(1, sum(L)+1):
        b[(i,0)] = False
    b[(L[0],0)] = True
    for k in range(1, len(L)):
        for x in range(sum(L)+1):
            if x-L[k] >= 0:
                b[(x,k)] = (b[(x-L[k],k-1)] or b[(x,k-1)])
            else:
                b[(x,k)] = b[(x,k-1)]
    return b
