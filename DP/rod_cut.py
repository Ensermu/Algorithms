x = {}
def cut_rod(w, v):
    if w < 1:   return 0
    if w not in x:
        for piece in range(1, w + 1):
            x_ = v[piece] + cut_rod(w - piece, v)
            if (w not in x) or (x[w] < x_):
                x[w] = x_
    return x[w]
