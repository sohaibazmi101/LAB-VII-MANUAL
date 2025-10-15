from collections import deque

grid = [
    [0,0,1,0],
    [0,0,0,0],
    [1,0,0,1],
    [0,0,0,0]
]
def bfs_robot_path(grid):
    start = (0,0)
    rows, cols = len(grid), len(grid[0])
    goal = (rows -1, cols - 1)
    directions = [(0, 1), (1, 0)]
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None
path = bfs_robot_path(grid)
if path:
    print("Path Found: ")
    print(path)
else:
    print("Path not found")