class PriorityQueue(object):
    def __init__(self):
        self.A = {}
        self.parent = {}
    def insert(self, label, key):
        self.A[label] = key
    def insert1(self, label, key):
        self.parent[label] = key
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
    
def MST_Prim(G, r):
    Q = PriorityQueue()
    for i in G:
        if i == r:
            Q.insert(i, 0)
        else:
            Q.insert(i, float('inf'))
        Q.insert1(i, None)
    while Q.A:
        u = Q.extract_min()
        for v in G[u]:
            if v in Q.A and G[u][v] < Q.A[v]:
                Q.parent[v] = u
                Q.A[v] = G[u][v]
    w = 0
    for i in Q.parent:
        if i != r:
            w += G[i][Q.parent[i]]
    print('weight of mst:', w)      
    return Q.parent