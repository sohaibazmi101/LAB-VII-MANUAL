import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_cell_cost(cell):
    if cell == 1:
        return float('inf') 
    elif cell == 'B':
        return 0.5          
    else:
        return 1           

def a_star_treasure(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start, [start]))
    visited = set()
    steps = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        steps += 1

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, visited, steps

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]
                cost = get_cell_cost(cell)
                if cost == float('inf'):
                    continue 
                neighbor = (nr, nc)
                if neighbor not in visited:
                    g_new = g + cost
                    f_new = g_new + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, visited, steps 
grid = [
    ['S', 0,   0,  'B', 'T'],
    [1,   1,   0,   1,   0 ],
    [0,   0,   0,   0,   0 ],
    [0,   1,   1,   1,   0 ],
    [0,   0,   0,   0,   0 ]
]

start = (0, 0)
goal = (0, 4)
numeric_grid = [[0 if cell in ['S', 'T'] else cell for cell in row] for row in grid]

path, visited, steps = a_star_treasure(numeric_grid, start, goal)

if path:
    print("Path found:")
    print(" -> ".join(map(str, path)))
else:
    print("Path not found.")

print("Visited nodes:", len(visited))
print("Steps taken:", steps)
