def Transitive_Closure(G):
    n = len(G)
    T = []*n
    for i in range(n):
        T.append([0]*n)
    for i in range(n):
        for j in range(n):
            if i == j or j+1 in G.get(i+1, {}):
                T[i][j] = 1
            else:
                T[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])
    return T