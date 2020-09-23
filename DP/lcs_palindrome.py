def lcs_palindrome(X):
    c = {}
    Y = list(X)
    Y.reverse()
    Y = "".join(Y)
    m = len(X)
    n = len(Y)
    for i in range(0, m+1):
        c[i,0] = 0
    for j in range(0, n+1):
        c[0,j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i,j] = c[i-1,j-1] + 1
            else:
                c[i,j] = max(c[i-1,j], c[i,j-1])
    return c[i,j]
