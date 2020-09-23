def alternate(a, i, j, b = {}):
    if (i, j) in b:
        return b[i, j]
    if i == j:
        return a[i]
    if i == j-1:
        return max(a[i], a[j])
    b[i, j] = max(min(alternate(i+1, j-1, b), alternate(i+2, j, b)) + a[i],
    			  min(alternate(i, j-2, b), alternate(i+1, j-1, b)) + a[j])
    return b[i, j]
