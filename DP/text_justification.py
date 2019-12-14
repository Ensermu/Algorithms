parent = {}
memo = {}
def text(i):
    if i >= n:
        return 0
    if i in memo:
        return memo[i]
    result = float('inf')
    for j in range(i+1, n+1):
        new = text(j) + badness(i,j)
        if new < result:
            result = new
            parent[i] = j
    memo[i] = result
    return result

def badness(a, b):
    page_width = 14
    total_length = 0
    for i in range(a, b):
        total_length += len(words[i])
    total_length += b - a - 1
    if total_length > page_width:
        return float('inf')
    badness = pow(page_width - total_length, 3)
    return badness
    
def print_optimal_way(i):
    way = []
    if i not in parent:
        return None
    while True:
        way.append(i)
        if parent.get(i) is None:
            break
        i = parent[i]
    return way
