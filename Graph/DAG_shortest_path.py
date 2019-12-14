def DFS(G):
    parent = {}
    visited = {}
    order = []
    for i in G:
        visited[i] = False
    for v in G:
        stack = []
        stack.append(v)
        if visited[v] is False:
            parent[v] = v
            while stack:
                u = stack.pop()
                if visited[u] is False:
                    visited[u] = True
                    for j in graph[u]:
                        parent[j] = u
                        stack.append(j) 
    for i in G:
        if graph[i] == {}:
            v = i
            while parent[v] != v:
                order.append(v)
                v = parent[v]
            order.append(v)
    order.reverse() 
    return order

def DAG_Shortest_Path(G, s):
    order = DFS(G)
    d = {}
    parent = {}
    for i in G.keys():
        d[i] = float('inf')
        parent[i] = None
    d[s], parent[s] = 0, s
    for u in order:
        for v in G[u]:
            if  d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u
    return d
