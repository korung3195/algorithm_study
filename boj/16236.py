import sys
from collections import deque
from copy import deepcopy

def solve():
    n = int(sys.stdin.readline())
    table = []
    SHARK = 9
    queue = deque()
    size = 2
    count = 0
    time = 0
    eatable = []
    x,y = 0,0
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    

    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        if SHARK in temp:
            shark_index = temp.index(SHARK)
            temp[shark_index] = 0
            x,y = i,shark_index
            queue.append((x,y))
            
        table.append(temp)

    visited = [[0 for _ in range(n)] for _ in range(n)]
    clock = 0
    while queue:
        clock += 1
        length = len(queue)
        for i in range(length):
            temp_x, temp_y = queue.popleft()

            if visited[temp_x][temp_y]:
                continue
            visited[temp_x][temp_y] = 1

            for j in range(4):
                new_x = temp_x+dx[j]
                new_y = temp_y+dy[j]

                if new_x < 0 or new_x >= n or new_y < 0 or new_y >=n:
                    continue

                if not visited[new_x][new_y] and (table[new_x][new_y] == 0 or table[new_x][new_y] == size):
                    queue.append((new_x,new_y))

                if 0<table[new_x][new_y]<size:
                    eatable.append((new_x,new_y))

        if eatable:
            target_x, target_y = sorted(eatable).pop(0)
            
            queue.clear()
            count += 1
            if count == size:
                count = 0
                size += 1

            table[target_x][target_y] = 0
            time += clock
            clock = 0
            x,y = target_x, target_y

            queue.append((x,y))
            eatable = []
            visited = [[0 for _ in range(n)] for _ in range(n)]

    return time

print(solve())