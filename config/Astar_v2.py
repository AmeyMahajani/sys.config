def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_simple(grid, start, goal):
    open_list = [start]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = min(open_list, key=lambda x: g_score[x] + heuristic(x, goal))

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)
        x, y = current

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue  # Wall
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    came_from[neighbor] = current
                    if neighbor not in open_list:
                        open_list.append(neighbor)
    return None

# Simple grid: 0 = free, 1 = obstacle
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

path = a_star_simple(grid, start, goal)
print("Path:", path)
