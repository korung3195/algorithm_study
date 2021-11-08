import sys
from collections import deque

n = int(sys.stdin.readline())
table = [[] for _ in range(n+1)]
res = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    table[x].append(y)
    table[y].append(x)

queue = deque()
queue.append(1)

while queue:
    parent = queue.popleft()
    children = table[parent]
    for child in children:
        if not res[child]:
            res[child] = parent
            queue.append(child)

print(*res[2:], sep='\n')

