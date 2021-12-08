import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
table = []
chickens = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
house = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if row[j] == 2:
            chickens.append((i,j))
        elif row[j] == 1:
            house += 1
    table.append(row)

chicken_dist = 10**6

def bfs(chicken_dist, chickens, house):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    count = 0
    sum = 0

    for x,y in chickens:
        visited[x][y] = True
        queue.append((x,y,0))

    while queue:
        x,y,dist = queue.popleft()
        
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue

            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist+1))

                if table[new_x][new_y] == 1:
                    count += 1
                    sum += dist+1
                
            if sum > chicken_dist:
                return sum

            if count >= house:
                return sum

comb = combinations(chickens, m)

for chk in comb:
    res = bfs(chicken_dist, chk, house)
    chicken_dist = min(chicken_dist,res)

print(chicken_dist)