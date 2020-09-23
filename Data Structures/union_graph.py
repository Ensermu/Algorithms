class Union_Find:
    def __init__(self):
        self.collection = []
        self.a = {}
    def add(self, x):
        self.collection.append(x)
    def remove(self, x):
        self.collection.remove(x)
    def __str__(self):
        return str([x.weight for x in self.collection])
                   
def Make_Set(x):
        new = Set()
        node = Node(x)
        node.parent = new
        new.head = node
        new.tail = node
        S.a[x] = node
        S.add(new)
        
def union(u, v):
    v = v.head
    S.remove(v.parent)
    while v:
        if u.tail.next is None:
            u.tail.next = v
        v.parent = u
        u.weight += 1
        if v.next is None:
            u.tail = v
        v = v.next

def Union(u, v):
    u = Find_Set(u)
    v = Find_Set(v)
    if u.weight >= v.weight:
        union(u, v)
    else:
        union(v, u)
        
def Find_Set(x):
    x = S.a[x]
    return x.parent

def Connected_Components(G):
    for i in G:
        Make_Set(i)
    for i in G:
        for j in G[i]:
            if Find_Set(i) != Find_Set(j):
                Union(i, j)
                
def Same_Component(u, v):
    if Find_Set(u) == Find_Set(v):
        return True
    return False

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.parent = None
        
class Set:
    def __init__(self):
        self.head = None
        self.tail = None
        self.weight = 1