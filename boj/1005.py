import sys
from collections import deque

read = sys.stdin.readline

def solve():
    n, k = map(int, read().split())
    weights = list(map(int, read().split()))
    edges = [[] for _ in range(n+1)]

    for _ in range(k):
        start, end = map(int, read().split())
        edges[end].append(start)

    w = int(read().strip())

    queue = deque([(w, weights[w-1])])
    times = [-1 for _ in range(n+1)]
    times[w] = weights[w-1]
    max_time = 0
    
    while queue:
        now, time = queue.popleft()
        if time < times[now]:
            continue
        
        max_time = max(time, max_time)

        for v in edges[now]:
            new_time = time+weights[v-1]
            if new_time > times[v]:
                times[v] = new_time
                queue.append((v, new_time))

    return max_time

t = int(read().strip())
for _ in range(t):
    print(solve())