graph_adj_list = {
    "A": ["B", "E", "D"],
    "B": ["A", "E", "C"],
    "C": ["B", "F"],
    "D": ["A", "G"],
    "E": ["A", "B", "H"],
    "F": ["C"],
    "G": ["D", "H"],
    "H": ["E", "G", "I"],
    "I": ["H"],
}


def dfs_traversal(adj_list, root):
    path = list()
    visited = set()
    stack = list()

    stack.append(root)

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            path.append(current_node)
            visited.add(current_node)
            stack.extend([new_node for new_node in adj_list[current_node]])

    return path


path = dfs_traversal(graph_adj_list, "A")
print(path)
