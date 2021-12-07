import sys
from collections import deque

def solve():
    a, b = map(int, sys.stdin.readline().split())
    queue = deque()

    queue.append((a, 0))

    while queue:
        num, count = queue.popleft()

        if num*2 == b or num*10+1 == b:
            return count+2

        if num*2 < b:
            queue.append((num*2, count+1))
        if num*10+1 < b:
            queue.append((num*10+1, count+1))

    return -1

print(solve())