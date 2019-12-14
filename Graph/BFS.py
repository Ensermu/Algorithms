from collections import deque
def BFS(G, s):
	parent = {}
	d = {}
	visited = {}
	queue = deque()
	queue.append(s)
	for i in G:
		parent[i] = None
		d[i] = float('inf')
		visited[i] = False
	visited[s] = True
	d[s] = 0
	while queue:
		u = queue.popleft()
		for v in G[u]:
			if visited[v] is False:
				parent[v] = u
				d[v] = d[u] + 1
				visited[v] = True
				queue.append(v)
	return d

