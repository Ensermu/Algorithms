X = {}
Y = {}
class Union_Find:
    def __init__(self):
        self.collection = []
        self.a = {}
    def add(self, x):
        self.collection.append(x)
    def remove(self, x):
        self.collection.remove(x)
    def __str__(self):
        return str(self.collection)  
        
def Make_Set(x):
    node = Node(x)
    node.parent = node
    S.a[x] = node
    S.add(node)
        
def Union(u, v):
    u = Find_Set(S.a[u])
    v = Find_Set(S.a[v])
    if u.height > v.height:
        v.parent = u
        S.remove(v)
    else:
        u.parent = v
        S.remove(u)
        if u.height == v.height:
            v.height = v.height + 1
        
def Find_Set(x):
    if x != x.parent:
        x.parent = Find_Set(x.parent)
    return x.parent

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.height = 0
S = Union_Find()

def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x for x in A.values()])
    D = [[] for i in range(u)]
    for x in A.keys():
        D[A[x]].append(x)
    i = 0
    B = [0]*(u-1)
    for chain in D:
        for x in chain:
            B[i] = x
            i += 1
    return B

def sort():
    for i in adj:
        for j in adj[i]:
            if (j, i) not in X:
                X[(i, j)] = adj[i][j]
    return counting_sort(X)

def MST_Kruskal(G):
    for v in G:
        Make_Set(v)
    Y = sort()
    A = []
    for i in Y:
        if Find_Set(S.a[i[0]]) != Find_Set(S.a[i[1]]):
            A.append((i[0], i[1]))
            Union(i[0], i[1])
    w = 0
    for i in A:
        w += adj[i[0]][i[1]]
    print('weight of mst:', w)      
    return A
