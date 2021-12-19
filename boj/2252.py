import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

degree = [0] * (n+1)
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    degree[b] += 1

queue = deque([i for i in range(1,n+1) if degree[i] == 0])

res = []

while queue:
    student = queue.popleft()
    
    if degree[student] == 0:
        res.append(student)

    for next in edges[student]:
        degree[next] -= 1
        if degree[next] == 0:
            queue.append(next)

print(*res)