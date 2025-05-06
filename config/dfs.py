visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
    for neighbour in graph[root]:
        if neighbour not in visited:
            dfs(visited, graph, neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

dfs(visited, graph, 'A')