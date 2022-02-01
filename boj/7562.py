import queue
import sys
from collections import deque

read = sys.stdin.readline
t = int(read().strip())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def solve():
    l = int(read().strip())
    visited = [[0 for _ in range(l)] for _ in range(l)]

    start_x, start_y = map(int, read().split())
    end_x, end_y = map(int, read().split())
    visited[start_x][start_y] = 1

    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, count = queue.popleft()

        if x == end_x and y == end_y:
            return count

        for i in range(8):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x < 0 or new_x >= l or new_y < 0 or new_y >= l or visited[new_x][new_y]:
                continue

            visited[new_x][new_y] = 1
            queue.append((new_x, new_y, count+1))


for _ in range(t):
    print(solve())