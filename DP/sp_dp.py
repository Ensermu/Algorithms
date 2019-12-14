class Graph(object):
    def __init__(self):
        self.adj = {}
        self.weight = {}
        self.indegree = {}
        self.num_vertices = []
    def add_edge(self, u, v, w):
        if self.adj.get(u) is None:
            self.adj[u] = []
        if self.indegree.get(v) is None:
            self.indegree[v] = []
        if u not in self.num_vertices and u != None:
            self.num_vertices.append(u)
        if v not in self.num_vertices and v != None:
            self.num_vertices.append(v)
        self.adj[u].append(v) 
        self.weight[(u,v)] = w
        self.indegree[v].append(u)

class ShortestPathResult(object): 
    def __init__(self):
        self.d = {}
        self.parent = {}
        
def shortest_path(graph, s, d):
    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None
    for v in graph.num_vertices:
        sp_dp(graph, v, result)
    return result.d[d]

def sp_dp(graph, v, result):
    if v in result.d:
        return result.d[v]
    result.d[v] = float("inf")
    result.parent[v] = None
    for u in graph.indegree[v]:
        if u != None: 
            new_distance = sp_dp(graph, u, result) + graph.weight[(u, v)]
            if new_distance < result.d[v]:
                result.d[v] = new_distance
                result.parent[v] = u
    return result.d[v]
