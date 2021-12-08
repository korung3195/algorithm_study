import sys
from collections import deque
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())
virus = []
blank = []
table = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
infected = 100

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)
    for j in range(m):
        if row[j] == 2:
            virus.append((i,j))
        elif row[j] == 0:
            blank.append((i,j))

def solve(infected, walls):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    temp_infected = 0
    
    for x, y in virus:
        queue.append((x,y))
        visited[x][y] = True

    while queue and temp_infected < infected:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue

            if (new_x, new_y) in walls:
                continue

            if table[new_x][new_y] == 0 and not visited[new_x][new_y]:
                temp_infected += 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

    return min(temp_infected, infected)


comb = combinations(blank, 3)

for walls in comb:
    infected = solve(infected, walls)

print(len(blank)-infected-3)