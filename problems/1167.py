import sys
from collections import deque

dist = dict()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    start = -1

    for i in range(len(temp)):
        if i == 0:
            start = temp[i]
            dist[start] = dict()
        elif temp[i] == -1:
            break
        elif i%2:
            dist[start][temp[i]] = temp[i+1]

queue = deque()
queue.append((1,0))
visited = [False] * (n+1)
visited[1] = True
end, end_dist = 1, 0

while queue:
    now, weight = queue.popleft()
    if end_dist < weight:
        end = now
        end_dist = weight

    for v in dist[now]:
        if not visited[v]:
            queue.append((v, weight+dist[now][v]))
            visited[v] = True

visited = [False] * (n+1)
visited[end] = True
queue.append((end,0))
end, end_dist = 1, 0

while queue:
    now, weight = queue.popleft()
    if end_dist < weight:
        end = now
        end_dist = weight

    for v in dist[now]:
        if not visited[v]:
            queue.append((v, weight+dist[now][v]))
            visited[v] = True

print(end_dist)
