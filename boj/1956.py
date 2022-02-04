import sys

read = sys.stdin.readline

v, e = map(int, read().split())

dist = [[float('inf') for _ in range(v+1)] for _ in range(v+1)]
edges = dict()

for _ in range(e):
    a, b, c = map(int, read().split())
    dist[a][b] = c

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

cycle = [dist[i][i] for i in range(1, v+1)]
min_cycle = min(cycle)

print(min_cycle if min_cycle != float('inf') else -1)