import math

class vEB:  
    def __init__(self, u):
        self.u = u
        self.min = None
        self.max = None
        self.cluster = []
        self.summary = None
        for i in range(int(pow(2, math.ceil(math.log2(u)/2)))):
            self.cluster.append(None)
        self.Recurse_cluster(u)
        self.Summary_Set(u)

    def Recurse_cluster(self, u):
        for i in range(int(pow(2, math.ceil(math.log2(u)/2)))):
            if u == 2:
                new = vEB_base(u)
            else:
                new = vEB(int(pow(2, math.log2(u)//2)))
            self.cluster[i] = new
            
    def Summary_Set(self, u):
        if u == 2:
            self.summary = vEB_base
        else:
            self.summary = vEB(int(pow(2, math.ceil(math.log2(u)/2))))
        
class vEB_base:
    def __init__(self, u):
        self.u = u
        self.min = None
        self.max = None
        
def index(V, i, j):
    return i * int(pow(2, math.log2(V.u)//2)) + j

def Tree_Minimum(V):
    return V.min

def Tree_Maximum(V):
    return V.max

def Empty_Tree_Insert(V, x):
    V.min = x
    V.max = x

def Tree_Member(V, x):
    high = int(x//int(pow(2, math.log2(V.u)//2)))
    low = x % int(pow(2, math.log2(V.u)//2))
    if x == V.min or x == V.max:
        return True
    elif V.u == 2:
        return False
    else:
        return Tree_Member(V.cluster[high], low)
    
def Tree_Insert(V, x):
    high = int(x//pow(2, math.log2(V.u)//2))
    low = x % int(pow(2, math.log2(V.u)//2))
    if V.min == None:
        Empty_Tree_Insert(V, x)
    else:
        if x < V.min:
            x, V.min = V.min, x
            high = int(x//pow(2, math.log2(V.u)//2))
            low = x % int(pow(2, math.log2(V.u)//2))
        if V.u > 2:
            if Tree_Minimum(V.cluster[high]) is None:
                Tree_Insert(V.summary, high)
                Empty_Tree_Insert(V.cluster[high], low)
            else:
                Tree_Insert(V.cluster[high], low)
        if x > V.max:
            V.max = x

def Tree_Insert_Multiple(V, l):
    for i in l:
        Tree_Insert(V, i) 
        
def Tree_Delete(V, x):
    high = int(x//int(pow(2, math.log2(V.u)//2)))
    low = x % int(pow(2, math.log2(V.u)//2))
    if V.min == V.max:
        V.min = None
        V.max = None
    elif V.u == 2:
        if x == 0:
            V.min = 1
        else:
            V.min = 0
        V.max = V.min
    else:
        if x == V.min:
            first_cluster = Tree_Minimum(V.summary)
            x = index(V, first_cluster, Tree_Minimum(V.cluster[first_cluster]))
            V.min = x
            high = int(x//int(pow(2, math.log2(V.u)//2)))
            low = x % int(pow(2, math.log2(V.u)//2))
        Tree_Delete(V.cluster[high], low)
        if Tree_Minimum(V.cluster[high]) is None:
            Tree_Delete(V.summary, high)
            if x == V.max:
                summary_max = Tree_Maximum(V.summary)
                if summary_max is None:
                    V.max = V.min
                else:
                    V.max = index(V, summary_max, Tree_Maximum(V.cluster[summary_max]))
        elif x == V.max:
            V.max = index(V, high, Tree_Maximum(V.cluster[high]))

def Tree_Successor(V, x):
    high = int(x//int(pow(2, math.log2(V.u)//2)))
    low = x % int(pow(2, math.log2(V.u)//2))
    if V.u == 2:
        if x == 0 and V.max == 1:
            return 1
        else:
            return None
    elif V.min is not None and x < V.min:
        return V.min
    else:
        max_low = Tree_Maximum(V.cluster[high])
        if max_low is not None and low < max_low:
            offset = Tree_Successor(V.cluster[high], low)
            return index(V, high, offset)
        else:
            succ_cluster = Tree_Successor(V.summary, high)
            if succ_cluster is None:
                return None
            else:
                offset = Tree_Minimum(V.cluster[succ_cluster])
                return index(V, succ_cluster, offset)
            
def Tree_Predecessor(V, x):
    high = int(x//int(pow(2, math.log2(V.u)//2)))
    low = x % int(pow(2, math.log2(V.u)//2))
    if V.u == 2:
        if x == 1 and V.min == 0:
            return 0
        else:
            return None
    elif V.max is not None and x > V.max:
        return V.max
    else:
        min_low = Tree_Minimum(V.cluster[high])
        if min_low is not None and low > min_low:
            offset = Tree_Predecessor(V.cluster[high], low)
            return index(V, high, offset)
        else:
            pred_cluster = Tree_Predecessor(V.summary, high)
            if pred_cluster is None:
                if V.min is not None and x > V.min:
                    return V.min
                else:
                    return None
            else:
                offset = Tree_Maximum(V.cluster[pred_cluster])
                return index(V, pred_cluster, offset)   