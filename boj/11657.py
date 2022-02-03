import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    edges = dict()

    for _ in range(m):
        v, u, w = map(int, sys.stdin.readline().split())
        
        if v not in edges:
            edges[v] = dict()

        weight = min(edges[v].get(u), w) if u in edges[v] else w
        edges[v].update({u:weight})

    dist = [float('inf')] * (n+1)
    dist[1] = 0

    for i in range(n):
        for x in edges:
            for y in edges[x]:
                if dist[x] != float('inf') and dist[y] > dist[x] + edges[x][y]:
                    if i == n-1:
                        print(-1)
                        return
                    dist[y] = dist[x] + edges[x][y]

    for d in range(2,n+1):
        if dist[d] == float('inf'):
            print(-1)
        else:
            print(dist[d])    

solve()
