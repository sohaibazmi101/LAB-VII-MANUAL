from collections import deque
def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    directions = ([-1, 0], [1, 0], [0, 1], [0, -1])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows) and (0 <= ny < cols) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None
maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0]
]
start = (0,0)
end = (4,4)
path = bfs_maze_solver(maze, start, end)
print(f"Shortest path of the maze: {path}")