class Graph(object):

    def __init__(self):
        self.adj = {}
        self.weight = {}
        self.indegree = {}
        self.parent = {}
    def add_edge(self, u, v, w):
        if self.adj.get(u) is None:
            self.adj[u] = []
        if self.indegree.get(v) is None:
            self.indegree[v] = []
        self.adj[u].append(v) 
        self.weight[(u,v)] = w
        self.indegree[v].append(u)

def short(s,v):
    graph.weight[(s,s)] = 0
    if (s,v) in res.keys():
        return res[(s,v)]
    if s == v:
        return 0
    result = float('inf')
    for i in graph.indegree[v]:
        new = short(s,i) + graph.weight[(i,v)]
        if new < result:        
            result = new
            graph.parent[v] = i
    res[(s,v)] = result
    return result

