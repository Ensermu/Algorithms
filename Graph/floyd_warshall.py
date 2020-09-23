def Set_Initial_Parent():
    n = len(adj)
    parent = []*n
    for i in range(n):
        parent.append([None]*n)
    for i in range(n):
        for j in range(n):
            if i == j or adj[i][j] == float('inf'):
                parent[i][j] = None
            elif i != j and adj[i][j] != float('inf'):
                parent[i][j] = i+1
    return parent
    
def Floyd_Warshall(W):
    n = len(W[0])
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] <= D[i][k] + D[k][j]:
                    parent[i][j] = parent[i][j]
                else:
                    parent[i][j] = parent[k][j]
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

def Print_SP(u, v):
    u -= 1
    v -= 1
    p = []
    p.append(v+1)
    while parent[u][v] != None:
        p.append(parent[u][v])
        v = parent[u][v] - 1
    p.reverse()
    return p