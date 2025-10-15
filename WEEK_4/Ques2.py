import heapq
import math
cities = {
    'A': (0,0),
    'B': (2,3),
    'C': (5,2),
    'D': (6,6),
    'E': (8,3)
}
graphs = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}
def euclidean(a,b):
    (x1, y1), (x2, y2) = cities[a], cities[b]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def best_first_search(start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (euclidean(start, goal), [start]))
    while pq:
        h, path = heapq.heappop(pq)
        city = path[-1]
        if city in visited:
            continue
        visited.add(city)
        if city == goal:
            return path
        for neighbor in graphs[city]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(pq, (euclidean(neighbor, goal), new_path))
    return None

start = 'A'
goal = 'E'
path = best_first_search(start, goal)
if path:
    print("Path found: ")
    print(" -> ".join(path))
else:
    print("No path found")