graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


def bfs(graph, root):
    if not graph or root not in graph:
        return
    
    visited, queue = set(), list()

    visited.add(root)
    queue.append(root)
    print(root)
    
    while queue:
        cur_node = queue.pop(0)

        for node in graph[cur_node] - visited:
            queue.append(node)
            visited.add(node)
            print(node)
    return


bfs(graph, '0')