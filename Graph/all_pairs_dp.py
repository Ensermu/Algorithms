def all_pairs_dp(G):
	d = {}
    for u in G.keys():
        d[u, u] = 0
        G[u][u] = 0
    for m in range(1, len(G)):
        for u in G.keys():
            for v in G.keys():
                for x in G.keys():
                    if d.get((u, v), float('inf')) > d.get((u, x), float('inf')) + G.get(x, {}).get(v, float('inf')):         
                        d[u, v] = d[u, x] + G[x][v]
    return d      