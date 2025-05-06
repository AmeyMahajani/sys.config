def bfs(visited, graph, queue):
    if not queue:
        return

    node = queue.pop(0)
    print(node)
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
   
    bfs(visited, graph, queue)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

queue = ['A']
visited = set()

bfs(visited, graph, queue)