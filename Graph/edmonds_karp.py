from collections import deque

def BFS(G, s, t):
    parent = {}
    visited = {}
    order = []
    minimum = float('inf')
    queue = deque()
    queue.append(s)
    for i in G:
        parent[i] = None
        visited[i] = False
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if visited[v] is False and G[u][v] != 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)

    v = parent[t]
    order.append(t)             
    while v:
        order.append(v)
        v = parent[v]
    order.reverse()
    for i in range(len(order)-1):
        if G[order[i]][order[i+1]] < minimum:
            minimum = G[order[i]][order[i+1]]
    return visited[t], minimum, order

def Edmonds_Karp(G, s, t):
    Gf = {}       
    for i in G:
        if i not in Gf:
            Gf[i] = {}
        for j in G[i]:
                Gf[i][j] = G[i][j][1] - G[i][j][0]
                if j not in Gf:
                    Gf[j] = {}
                Gf[j][i] = G[i][j][0]
    while BFS(Gf, 's', 't')[0]:
        path = BFS(Gf, 's', 't')    
        order = path[2]
        for i in range(len(order)-1):
            Gf[order[i]][order[i+1]] -= path[1]
            Gf[order[i+1]][order[i]] += path[1]
    return Gf

def Print_Graph(Gff):
    G = {}
    max_flow = 0
    for i in adj:
        if i not in G:
            G[i] = {}
        for j in adj[i]:
                G[i][j] = adj[i][j][1] - Gff[i][j]
                if j not in G:
                    G[j] = {}
    for i in G['s'].values():
        max_flow += i
    return max_flow