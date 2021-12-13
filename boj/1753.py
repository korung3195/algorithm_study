import sys, math
import heapq

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())

edges = dict()
graph = [math.inf for _ in range(v+1)]
visited = [False for _ in range(v+1)]
queue = []

graph[start] = 0

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    if u in edges:
        if v in edges[u]:
            edges[u][v] = min(w, edges[u][v])
        else:
            edges[u][v] = w
    else:
        edges[u] = {v:w}

heapq.heappush(queue, (0, start))

while queue:
    weight, now = heapq.heappop(queue)
    if visited[now]:
        continue
    visited[now] = True

    if not (now in edges):
        continue

    for v in edges.get(now):
        new_weight = weight + edges.get(now).get(v)
        if not visited[v] and graph[v] > new_weight:
            graph[v] = new_weight
            heapq.heappush(queue, (new_weight, v))
    
for i in graph[1:]:
    if i==math.inf:
        print("INF")
    else:
        print(i)