def Edit(X, Y):
    c = {}
    m = len(X)
    n = len(Y)
    for i in range(0, m+1):
        c[i,0] = i
    for j in range(0, n+1):
        c[0,j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1] and c[i-1,j-1] <= c[i,j-1] + 1 and c[i-1,j-1] <= c[i-1,j] + 1:
                c[i,j] = c[i-1,j-1]
            elif X[i-1] != Y[j-1] and c[i-1,j-1] + 2 <= c[i,j-1] + 1 and c[i-1,j-1] + 2 <= c[i-1,j] + 1:
                c[i,j] = c[i-1,j-1] + 2
            elif c[i,j-1] + 1 <= c[i-1,j] + 1:
                c[i,j] = c[i,j-1] + 1
            else:
                c[i,j] = c[i-1,j] + 1
    return c[i,j]
