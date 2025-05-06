import heapq

def prims(graph, start):

    visited = set()
    min_heap = [(0, start)]
    total_weight = 0

    print("Edges in the MST: ")
    print("The starting node is: ", start)

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_weight+=weight
        if weight != 0:
            print(f"pick an edge with weight {weight} leading to {u}")

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))


    print("total weight of the MST is: ", total_weight)


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prims(graph, 'A')