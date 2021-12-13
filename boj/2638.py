import sys

sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = set()

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(visited, x,y):
    global flag
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue

        if not table[new_x][new_y] and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            dfs(visited, new_x, new_y)
        
        if table[new_x][new_y]:
            if (new_x,new_y) in check:
                visited[new_x][new_y] = True
                table[new_x][new_y] = 0
                flag = True
            check.add((new_x,new_y))
            

flag = True
count = 0
while flag:
    flag = False
    check.clear()
    count += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    dfs(visited, 0,0)

print(count-1)

