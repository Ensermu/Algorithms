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
    new = Set()
    node = Node(x)
    node.parent = node
    S.a[x] = node
    S.add(new)
        
def Union(u, v):
    v = Find_Set(v)
    u = Find_Set(u)
    S.remove(v)
    if u.height > v.height:
        v.parent = u
    else:
        u.parent = v
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
 
class Set:
    def __init__(self):
        self.height = 0