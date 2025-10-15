import heapq
grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0]
]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_start(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path
        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                if neighbor not in visited:
                    g_new = g + 1
                    f_new = g_new + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))
    return None
start = (0,0)
goal = (3,3)
path = a_start(grid, start, goal)
if path:
    print("Path found: ", path)
else:
    print("Path not found")