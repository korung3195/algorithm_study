import sys, heapq

def dijkstra(edges, x, n):
    INF = 10**9
    dist = [INF] * (n+1)
    queue = [(0, x)]
    dist[x] = 0

    while queue:
        weight, now = heapq.heappop(queue)
        
        if weight > dist[now]:
            continue
        if now not in edges:
            continue

        for v in edges[now]:
            if dist[now] + edges[now][v] < dist[v]:
                dist[v] = dist[now] + edges[now][v]
                heapq.heappush(queue,(dist[v], v))
    
    return dist

n, m, x = map(int, sys.stdin.readline().split())
edges = dict()
rev_edges = dict()

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    if a not in edges:
        edges[a] = dict()
    if b not in rev_edges:
        rev_edges[b] = dict()
    edges[a][b] = w
    rev_edges[b][a] = w

dist = dijkstra(edges, x, n)
rev_dist = dijkstra(rev_edges, x, n)

res = 0
for i in range(1, n+1):
    if dist[i] + rev_dist[i] > res:
        res = dist[i] + rev_dist[i]
print(res)
