def optimal_bst(i, j, b = {}):
    if (i, j) in b:
        return b[i, j]
    if i == j:
        return 0
    if i == j-1:
        return a[i]
    result = float('inf')
    for r in range(i, j):
        new = optimal_bst(i, r, b) + optimal_bst(r+1, j, b) + sum(a[i:j])
        if  new < result:
            c[i, j] = r
            result = new
    b[i, j] = result
    return result