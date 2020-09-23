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

def Bellman_Ford(G, s):
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
                return False
    return True

def Johnson(G):
    n = len(G)
    p = []
    G['s'] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    parent = []*n
    for i in range(n):
        parent.append([None]*n)
    if Bellman_Ford(G, 's') == False:
        print('negative weight cycle')
    else:
        for i in G.keys():
            h[i] = d[i]
        for i in G.keys():
            for j in G[i]:
                if i != 's':
                    G[i][j] = G[i][j] + h[i] - h[j]
        n = (len(G)-1)
        D = []*n
        for i in range(n):
            D.append([float('inf')]*n)
        for i in G:
            t = Dijkstra(G, i)
            d1 = t[0]
            p.append(t[1])
            for j in G:
                if j != 's' and i != 's':
                    D[i-1][j-1] = d1[j] + h[j] - h[i]
    k = -1
    for i in p:
        k += 1
        if k == 5:
            break
        for j in i:
            if j != 's':
                if i[j] != j:
                    parent[k][j-1] = i[j]
            
    return D, parent

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