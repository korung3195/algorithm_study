import sys

MAX_DIST = 1000000000

def solve():
    n, m, w = map(int, sys.stdin.readline().split())
    dist = [MAX_DIST] * (n+1)
    dist[1] = 0
    vertex = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        vertex[s].append((e,t))
        vertex[e].append((s,t))

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        vertex[s].append((e,-t))

    for i in range(1,n+1):
        for s in range(1,n+1):
            for e, t in vertex[s]:
                if dist[e] > dist[s] + t:
                    if i == n:
                        return "YES"
                    dist[e] = dist[s] + t
    
    return "NO"

t = int(sys.stdin.readline().strip())

for _ in range(t):
    print(solve())