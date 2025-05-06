graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
assigned = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if assigned.get(neighbor) == color:
            return False
    return True

def color_graph(nodes, index=0):
    if index == len(nodes):
        return True

    node = nodes[index]
    for color in colors:
        if is_safe(node, color):
            assigned[node] = color
            if color_graph(nodes, index + 1):
                return True
            del assigned[node]  # backtrack
    return False

nodes = list(graph.keys())

if color_graph(nodes):
    print("Color assignment:")
    for node in nodes:
        print(f"{node} -> {assigned[node]}")
else:
    print("No valid coloring found.")
