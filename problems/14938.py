import sys

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
vertex = dict()
INF = 10**6
dist = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(r):
    a, b, w = map(int, sys.stdin.readline().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], w)
    dist[b-1][a-1] = min(dist[b-1][a-1], w)
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k])

res = [0] * n

for i in range(n):
    for j in range(n):
        if dist[i][j] <= m:
            res[i] += items[j]

print(max(res))