import sys, heapq

n, e = map(int, sys.stdin.readline().split())
vertex = dict()
INF = 10**9

for _ in range(e):
    x, y, weight = map(int, sys.stdin.readline().split())

    if x not in vertex:
        vertex[x] = dict()
    if y in vertex[x]:
        vertex[x][y] = min(weight, vertex[x][y])
    else:
        vertex[x][y] = weight

    if y not in vertex:
        vertex[y] = dict()
    if x in vertex[y]:
        vertex[y][x] = min(weight, vertex[y][x])
    else:
        vertex[y][x] = weight

def dijkstra(start, end1, end2, vertex):
    dist = [INF] * (n+1)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        weight, now = heapq.heappop(queue)
        if weight > dist[now]:
            continue

        if now not in vertex:
            continue

        for v in vertex[now]:
            if dist[now] + vertex[now][v] < dist[v]:
                dist[v] = dist[now] + vertex[now][v]
                heapq.heappush(queue,(dist[v],v))
    
    return [dist[1], dist[end1], dist[end2]]

point_a, point_b = map(int, sys.stdin.readline().split())
dist_a = dijkstra(point_a, point_b, n, vertex)
dist_b = dijkstra(point_b, point_a, n, vertex)

sum_a = [dist_a[0], dist_a[1], dist_b[2]]
sum_b = [dist_b[0], dist_b[1], dist_a[2]]

if sum(sum_a) < sum(sum_b):
    if INF in sum_a:
        print(-1)
    else:
        print(sum(sum_a))
else:
    if INF in sum_b:
        print(-1)
    else:
        print(sum(sum_b))