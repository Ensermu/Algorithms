def Bellman_Ford(G, s):
    d = {}
    parent = {}
    for i in G:
        d[i] = float('inf')
    d[s] = 0
    for i in range(len(G)):
        for u in G:
            for v in G[u]:
                if d[v] > d[u] + G[u][v]:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u
    for u in G:
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                print('negative weight cycle')
    return d
