parent = {}
def DFS_Visit(s, graph):
    if s in graph.keys():
       for v in graph[s]:
           if v not in parent:
               parent[v] = s
               DFS_Visit(v, graph)
               
def DFS(v, graph):
    for s in graph.keys():
        if s not in parent:
            parent[s] = None
            DFS_Visit(s, graph)
    return parent

