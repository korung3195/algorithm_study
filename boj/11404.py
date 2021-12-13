import sys

bus = dict()

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

dist = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    dist[u-1][v-1] = min(dist[u-1][v-1], w)

for k in range(n):
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

for dst in dist:
    for num in dst:
        if num == float('inf'):
            print(0, end=" ")
        else:
            print(num, end=" ")
    print()