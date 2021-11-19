import sys
from collections import deque

n = int(sys.stdin.readline().strip())
dist = dict()
queue = deque()
visited = [False] * (n+1)

for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())

    if u in dist:
        dist[u][v] = w
    else:
        dist[u] = dict()
        dist[u][v] = w
    
    if v in dist:
        dist[v][u] = w
    else:
        dist[v] = dict()
        dist[v][u] = w

queue.append((1,0))
max_weight = 0
max_point = 1
visited[1] = 0

while queue:
    now, weight = queue.popleft()
    flag = False

    if not now in dist:
        continue

    for v in dist[now]:
        if not visited[v]:
            visited[v] = True
            queue.append((v,weight + dist[now][v]))
            flag = True

    if not flag and max_weight < weight:
        max_weight = weight
        max_point = now

visited = [False] * (n+1)
visited[max_point] = True
queue.append((max_point,0))

while queue:
    now, weight = queue.popleft()

    flag = False

    if not now in dist:
        continue

    for v in dist[now]:
        if not visited[v]:
            visited[v] = True
            queue.append((v,weight + dist[now][v]))
            flag = True

    if not flag and max_weight < weight:
        max_weight = weight

print(max_weight)