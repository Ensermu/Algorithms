def jump(b, s, n, v):
    m = int(math.sqrt(n))
    for i in range(s, n, m):
        if v < b[i]:
            for j in range(i-4, i):
                if v == b[j]:
                    return True
        if n-1 < i+m:
            for k in range(len(b)-m, len(b)):
                if v == b[k]:
                    return True
        if v == b[i]:
            return True
    return False
