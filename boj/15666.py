import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
res = set()
temp = []

def track(count, start):
    if count == 0:
        res.add(tuple(temp))
        return
    for i in range(start, n):
        temp.append(numbers[i])
        track(count-1, i)
        temp.pop()

track(m, 0)

for num in sorted(res):
    print(*num)
