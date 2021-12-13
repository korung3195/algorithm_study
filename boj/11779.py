import sys, heapq
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

edges = dict()

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    
    if start not in edges:
        edges[start] = dict()
    if end not in edges[start]:
        edges[start][end] = cost
    else:
        edges[start][end] = min(edges[start][end], cost)

start, end = map(int, sys.stdin.readline().split())

INF = 10**12
dist = [(INF, None) for _ in range(n+1)]
dist[start] = (0, None)
queue = [(0, start)]

while queue:
    cost, now = heapq.heappop(queue)

    if dist[now][0] < cost:
        continue
    if now not in edges:
        continue

    for v in edges[now]:
        if dist[v][0] > dist[now][0] + edges[now][v]:
            dist[v] = (dist[now][0] + edges[now][v], now)
            heapq.heappush(queue, (dist[v][0], v))

count = 0
track = deque([end])

point = dist[end]
while point[1] != start:
    count += 1
    track.appendleft(point[1])
    point = dist[point[1]]

track.appendleft(start)

print(dist[end][0])
print(count+2)
print(*track)