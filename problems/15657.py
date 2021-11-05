import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
table = list(map(int, sys.stdin.readline().split()))
table.sort()

answer = deque()

def track(start, count):
    if count == 0:
        print(" ".join(map(str,answer)))
        return

    for i in range(start, n):
        answer.append(table[i])
        track(i, count-1)
        answer.pop()
    
track(0, m)