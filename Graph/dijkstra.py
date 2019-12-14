class PriorityQueue(object):
    def __init__(self):
        self.A = {}
    def insert(self, label, key):
        self.A[label] = key
    def extract_min(self):
        min_label = None
        for label in self.A:
            if (min_label is None) or (self.A[label] < self.A[min_label]):
                min_label = label
        del self.A[min_label]
        return min_label
    def decrease_key(self, label, key):
        if key < self.A[label]:
            self.A[label] = key
    def __str__(self):
    	return str(self.A)
    	
def Dijkstra(G, s):
    d = {}
    parent = {}
    for i in G:
        d[i] = float('inf')
    for i in G:
        parent[i] = None
    d[s], parent[s] = 0, s
    Q = PriorityQueue()
    for v in G:
        Q.insert(v, d[v])
    for _ in range(len(G)):
        u = Q.extract_min()
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u
                Q.decrease_key(v, d[v])
    return d, parent           

