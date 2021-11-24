import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    table = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

    queue = deque()
    queue.append((0,0,1,True))
    table[0][0] = 2

    dx = [1,0,0,-1]
    dy = [0,1,-1,0]

    while queue:
        x, y, dist, brokable = queue.popleft()
        
        if x == n-1 and y == m-1:
            return dist

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue

            if brokable:
                if table[new_x][new_y] == 1:
                    queue.append((new_x,new_y,dist+1,False))
                elif table[new_x][new_y] <= 0:
                    table[new_x][new_y] = 2
                    queue.append((new_x,new_y,dist+1,True))
            elif table[new_x][new_y] == 0:
                table[new_x][new_y] = -1
                queue.append((new_x,new_y,dist+1,False))

    return -1

print(solve())
