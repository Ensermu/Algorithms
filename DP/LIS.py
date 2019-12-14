memo = {}
parent = {}
order = []
def find(L):
    '''the longest increasing sequence'''
    for i in range(0,len(L)):
        memo[i] = 1
    for i in range(len(L)-1, -1, -1):
        for j in range(i+1,len(L)):
            if L[j] > L[i]:
                new = 1 + memo[j]
                if new > memo[i]:
                    memo[i] = new
                    parent[i] = j
    return max(memo.values())
    
def print_optimal_way():
    k = 0
    for i in memo.keys():
        if memo[i] > k:
            k = memo[i]
            start = i
    while True:
        if start not in parent:
            order.append(start)
            break
        order.append(start)
        start = parent[start]
    return order
