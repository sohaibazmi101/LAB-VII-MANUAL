from collections import deque
import heapq
maze = [
    ['S', 0, 1, 0, 'G'],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (0, 4)
rows, cols = len(maze), len(maze[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] != 1

def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    steps = 0

    while queue:
        current = queue.popleft()
        steps += 1
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, visited, steps

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    return None, visited, steps

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal):
    heap = []
    heapq.heappush(heap, (0 + manhattan_dist(start, goal), 0, start))
    parent = {start: None}
    g_score = {start: 0}
    visited = set()
    steps = 0

    while heap:
        f, g, current = heapq.heappop(heap)
        steps += 1

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, visited, steps

        visited.add(current)

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)
            if is_valid(nr, nc) and neighbor not in visited:
                tentative_g_score = g + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + manhattan_dist(neighbor, goal)
                    heapq.heappush(heap, (f_score, tentative_g_score, neighbor))

    return None, visited, steps

bfs_path, bfs_visited, bfs_steps = bfs(start, goal)
print("BFS:")
print("Path:", bfs_path)
print("Visited nodes:", len(bfs_visited))
print("Steps taken:", bfs_steps)

astar_path, astar_visited, astar_steps = astar(start, goal)
print("\nA*:")
print("Path:", astar_path)
print("Visited nodes:", len(astar_visited))
print("Steps taken:", astar_steps)