import heapq

class Graph(object):
    def __init__(self):
        self.adj = {}
        self.weight = {}
    def add_edge(self, u, v, w):
        if self.adj.get(u) is None:
            self.adj[u] = []
        self.adj[u].append(v) 
        self.weight[(u,v)] = w

def Dijkstra(g):
    s = []
    Q = []
    for i in relax.keys():
        heapq.heappush(Q, i)
    while Q != []:
         a = heapq.heappop(Q)
         s.append(a)
         u = relax[a]
         for j in graph1.adj[u]:
            if j is None:
                break
            if j not in relax.values():
                parent[j] = u
                relax[a + graph1.weight[u,j]] = j
                relax1[j] = a + graph1.weight[u,j]
                heapq.heappush(Q, a + graph1.weight[u, j])
            else:
                if relax1[j] > relax1[u] + graph1.weight[u, j]:
                    parent[j] = u
                    c =- 1
                    for b in Q:
                        c += 1
                        if b == relax1[j]:
                            Q[c] = relax1[u] + graph1.weight[u, j]
                            break
                    relax1[j] = relax1[u] + graph1.weight[u, j]
                    relax[a + graph1.weight[u,j]] = j
    return relax1
