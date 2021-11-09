import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
visited = [0] * n

res = set()
temp = deque()

def track(left):
    if left == 0:
        res.add(tuple(temp))
        return
    for i in range(n):
        if not visited[i]:
            temp.append(numbers[i])
            visited[i] = 1
            track(left-1)
            temp.pop()
            visited[i] = 0

track(m)

for x in sorted(res):
    print(*x)