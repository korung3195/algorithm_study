import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())

    table = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    table[0][0] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque([(0,0,1)])

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or not table[new_x][new_y]:
                continue

            if new_x == n-1 and new_y == m-1:
                return count+1

            table[new_x][new_y] = 0
            queue.append((new_x, new_y, count+1))
    
print(solve())
