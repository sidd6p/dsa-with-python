"""
Time Complexity:
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| DFS       | O(1)      | O(V + E)     | O(V + E)   |
| BFS       | O(1)      | O(V + E)     | O(V + E)   |

Space Complexity:
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| DFS       | O(V)      | O(V)         | O(V)       |
| BFS       | O(V)      | O(V)         | O(V)       |
"""

from collections import deque

def dfs(graph, start, end):
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



def bfs(graph, start, end):
    if start not in graph or end not in graph:
        return False 

    queue, visited = deque([start]), set()

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        if current not in visited:
            visited.add(current)
            queue.extend(graph.get(current, []))

    return False
