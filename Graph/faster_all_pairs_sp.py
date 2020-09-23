def Extended_SP(L, W):
    n = len(L[0])
    X = []*n
    for i in range(n):
        X.append([float('inf')]*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                X[i][j] = min(X[i][j], L[i][k] + W[k][j])
    return X

def Faster_All_Pairs_SP(W):
    n = len(W[0])
    L = W
    m = 1
    while m < n-1:
        L = Extended_SP(L, L)
        m = 2*m
    return L