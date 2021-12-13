import sys
from collections import deque

INF = 10**5
n, m = map(int, sys.stdin.readline().split())
dist = [INF] * 100001

dist[n] = 0
queue = deque()
queue.append((n, 0))
count, flag = 0, 0

while queue:
    now, time = queue.popleft()
    if now == m:
        if not count:
            flag = time
        count += 1

    if count:
        if flag < time:
            break
        continue

    if now <= INF/2 and dist[now*2] in (INF, time+1):
        dist[now*2] = time+1
        queue.append((now*2, time+1))
    if now < INF and dist[now+1] in (INF, time+1):
        dist[now+1] = time+1
        queue.append((now+1, time+1))
    if now > 0 and dist[now-1] in (INF, time+1):
        dist[now-1] = time+1
        queue.append((now-1, time+1))

print(flag, count, sep="\n")