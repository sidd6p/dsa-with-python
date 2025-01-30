def dfs(graph, root, visited = None):
    if visited is None:
        visited = set()
    visited.add(root)
    print(root)

    for node in graph[root] - visited:
        dfs(graph, node, visited)


    return 


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


dfs(graph, "0")
