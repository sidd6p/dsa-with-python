graph_adj_list =  {
    "A": ["B", "E", "D"],
    "B": ["A", "E", "C"],
    "C": ["B", "F"],
    "D": ["A", "G"],
    "E": ["A", "B", "H"],
    "F": ["C"],
    "G": ["D", "H"],
    "H": ["E", "G", "I"],
    "I": ["H"]
}

def dfs_traversal(adj_list, root, path, visited=None):
    if visited is None:
        visited = set()

    if root not in visited:
        visited.add(root)
        path.append(root)
        
        for node in adj_list[root]:
            dfs_traversal(adj_list, node, path, visited)

    return path

path = list()
dfs_traversal(graph_adj_list, "A", path)
print(path)