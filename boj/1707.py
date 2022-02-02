import sys
from collections import deque

read = sys.stdin.readline
k = int(read().strip())

def solve():
    v, e = map(int, read().split())
    edges = dict()
    division = [0] * (v+1)
    queue = deque([])
    
    for _ in range(e):
        a, b = map(int, read().split())

        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []

        edges[a].append(b)
        edges[b].append(a)
    
    for i in range(1, v+1):
        if division[i] == 0:
            division[i] = 1
        queue.append((i,division[i]))

        while queue:
            now, div = queue.popleft()

            if now not in edges:
                continue

            for dest in edges[now]:
                if division[dest] * div > 0:
                    return "NO"
                
                if division[dest] == 0:
                    division[dest] = -1 * div
                    queue.append((dest, division[dest]))
        
    return "YES"

for _ in range(k):
    print(solve())