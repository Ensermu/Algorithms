c = {}
b = {}
parent = {}
order = []
def Longest_Common_Subsequence(X, Y):
    m = len(X)
    n = len(Y)
    for i in range(0, m+1):
        c[i,0] = 0
    for j in range(0, n+1):
        c[0,j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i,j] = c[i-1, j-1]+1
                b[i,j] = 'd'
            elif c[i-1,j] >= c[i, j-1]:
                c[i,j] = c[i-1, j]
                b[i,j] = 'u'
            else:
                c[i,j] = c[i, j-1]
                b[i,j] = 'l'
    return c[i, j]

def Print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return 
    if b[i,j] == 'd':
        order.append(X[i-1])
        Print_LCS(b, X, i-1, j-1)
    elif b[i,j] == 'u':
        Print_LCS(b, X, i-1, j)
    else:
        Print_LCS(b, X, i, j-1)
    return order
