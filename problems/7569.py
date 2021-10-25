import sys
from collections import deque

def solve():
    m, n, h = map(int,sys.stdin.readline().strip().split())

    table = [[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]
    queue = deque()
    count = m*n*h
    flag = True

    dx = [0,0,0,0,1,-1]
    dy = [0,0,1,-1,0,0]
    dz = [1,-1,0,0,0,0]

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if table[z][y][x] == 1:
                    table[z][y][x] = -1
                    queue.append((x,y,z))
                if table[z][y][x] == 0:
                    flag = False
                    count -= 1

    if (flag):
        return 0

    day = -1
    while queue:
        length = len(queue)
        for _ in range(length):
            x,y,z = queue.popleft()
            for i in range(6):
                if 0<=x+dx[i]<m and 0<=y+dy[i]<n and 0<=z+dz[i]<h and table[z+dz[i]][y+dy[i]][x+dx[i]] == 0:
                    table[z+dz[i]][y+dy[i]][x+dx[i]] = -1
                    count += 1
                    queue.append((x+dx[i],y+dy[i],z+dz[i]))
        day += 1

    return day if count == m*n*h else -1

print(solve())