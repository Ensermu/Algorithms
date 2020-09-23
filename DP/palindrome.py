def palindrome(X, i, j, p = {}):
    if (X, i, j) in p:
        return p[(X, i, j)]
    if i == j: 
        return 1
    if X[i] == X[j]:
        if i+1 == j: 
            return 2
        else:
            result = 2 + palindrome(X, i+1, j-1, p)
    else:
        result = max(palindrome(X, i+1,j, p), palindrome(X, i, j-1, p))
    p[(i, j)] = result
    return result
