# BFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited

start_node = 'A'
print("BFS Traversal:", " -> ".join(bfs(graph, start_node)))


# DFS

def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited

start_node = 'A'
print("DFS Traversal:", " -> ".join(dfs(graph, start_node)))
