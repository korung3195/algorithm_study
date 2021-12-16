import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque([(n,0)])
table = [-1] * (10**6+1)

while queue:
    now, count = queue.popleft()
    if now == 1:
        break
    if not now%3 and table[now//3] < 0:
        table[now//3] = now
        queue.append((now//3, count+1))
    if not now%2 and table[now//2] < 0:
        table[now//2] = now
        queue.append((now//2, count+1))
    if now > 1 and table[now-1] < 0:
        table[now-1] = now
        queue.append((now-1, count+1))

print(count)
index = 1
res = []
while index < n:
    res.append(index)
    index = table[index]
res.append(n)

print(*res[::-1])