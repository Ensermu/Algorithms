def DFS(G, s, t):
    parent = {}
    visited = {}
    order = []
    minimum = float('inf')
    for i in G:
        visited[i] = False
    stack = []
    stack.append(s)
    parent[s] = s
    while stack:
        u = stack.pop()
        if visited[u] is False:
            visited[u] = True
            for j in G[u].keys():
                if G[u][j] != 0 and j not in parent:
                    parent[j] = u
                    stack.append(j) 
    v = t  
    if visited[t]:             
        while v != parent[v]:
            order.append(v)
            v = parent[v]
        order.append(v)
    order.reverse() 
    for i in range(len(order)-1):
        if G[order[i]][order[i+1]] < minimum:
            minimum = G[order[i]][order[i+1]]
    return visited[t], minimum, order

def Ford_Fulkerson(G, s, t):
    Gf = {}       
    for i in G:
        if i not in Gf:
            Gf[i] = {}
        for j in G[i]:
                Gf[i][j] = G[i][j][1] - G[i][j][0]
                if j not in Gf:
                    Gf[j] = {}
                Gf[j][i] = G[i][j][0]
    while DFS(Gf, 's', 't')[0]:
        path = DFS(Gf, 's', 't')    
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
    return max_flow, G