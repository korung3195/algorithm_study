import sys
from collections import deque

n, c = map(int, sys.stdin.readline().split())
table = deque()
for _ in range(n):
    table.append(int(sys.stdin.readline().strip()))

table = sorted(table)
start, end = 0, 1000000000
res = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    before = 0

    for i in range(1, n):
        if table[i] - table[before] >= mid:
            count += 1
            before = i

    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        res = mid

print(res)