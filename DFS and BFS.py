"""
DFS and BFS Search (Iterative & Recursive)

| Algorithm                | Best Case | Average Case | Worst Case |
|--------------------------|-----------|--------------|------------|
| DFS (Iterative & Recursive) | O(1)      | O(V + E)     | O(V + E)   |
| BFS (Iterative & Recursive) | O(1)      | O(V + E)     | O(V + E)   |
"""

from collections import deque

# Depth-First Search (DFS) - Iterative
def dfs_iterative(graph, start, end):
    if start not in graph or end not in graph:
        return False  

    stack, visited = [start], set()

    while stack:
        current = stack.pop()
        if current == end:
            return True
        if current not in visited:
            visited.add(current)
            stack.extend(graph.get(current, []))

    return False

    # Time Complexity: O(V + E)


# Depth-First Search (DFS) - Recursive
def dfs_recursive(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    if node == target:
        return True
    if node in visited:
        return False

    visited.add(node)
    for neighbor in graph.get(node, []):
        if dfs_recursive(graph, neighbor, target, visited):
            return True
    return False
    # Time Complexity: O(V + E)


# Breadth-First Search (BFS) - Iterative
def bfs_iterative(graph, start, target):
    if start not in graph or end not in graph:
        return False 

    queue = deque([start])
    visited = set()

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        if current not in visited:
            visited.add(current)
            queue.extend(graph.get(current, []))

    return False
    # Time Complexity: O(V + E)


# Breadth-First Search (BFS) - Recursive
def bfs_recursive(graph, queue, target, visited=None):
    if not queue:
        return False

    if visited is None:
        visited = set()

    node = queue.popleft()
    if node == target:
        return True
    if node not in visited:
        visited.add(node)
        queue.extend(graph.get(node, []))

    return bfs_recursive(graph, queue, target, visited)
    # Time Complexity: O(V + E)
