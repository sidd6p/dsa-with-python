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
def dfs_recursive(graph, start, target, visited=None):
    if start not in graph or target not in graph:
        return False

    if visited is None:
        visited = set()
    if start == target:
        return True
    if start in visited:
        return False

    visited.add(start)
    for neighbor in graph.get(start, []):
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
    if start not in graph or target not in graph:
        return False

    if visited is None:
        visited = set()
    if queue is None:
        queue = deque([start])
    if not queue:
        return False  

    current = queue.popleft()
    if current == target:
        return True

    if current not in visited:
        visited.add(current)
        queue.extend(graph.get(current, []))

    return bfs_recursive(graph, start, target, queue, visited)
    # Time Complexity: O(V + E)
