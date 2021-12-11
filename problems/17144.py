import sys

r, c, t = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

upper_dx = [-1,0,1,0]

while t > 0:
    temp = [[0 for _ in range(c)] for _ in range(r)]
    t -= 1

    for i in range(r):
        for j in range(c):
            if room[i][j] <= 0:
                continue

            count = 0
            mount = room[i][j] // 5

            for k in range(4):
                new_x = i+dx[k]
                new_y = j+dy[k]
                if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
                    continue
                if room[new_x][new_y] < 0:
                    continue
                count += 1
                temp[new_x][new_y] += mount
            
            temp[i][j] += - mount * count

    lower = (0,0)
    for i in range(r):
        for j in range(c):
            if room[i][j] < 0:
                lower=(i,j)
            room[i][j] += temp[i][j]

    upper = (lower[0]-1, lower[1])
    lower = (lower[0], lower[1])

    index = 0
    point = (lower[0]+1, lower[1])

    while True:
        if point[0]+dx[index] < lower[0] or point[0]+dx[index] >= r or point[1]+dy[index] < 0 or point[1]+dy[index] >= c:
            index += 1
        
        new_x = point[0]+dx[index]
        new_y = point[1]+dy[index]

        if room[new_x][new_y] < 0:
            room[point[0]][point[1]] = 0
            break

        room[point[0]][point[1]] = room[new_x][new_y] 
        point = (new_x,new_y)

    point = (upper[0]-1, upper[1])
    index = 0

    while True:
        if point[0]+upper_dx[index] < 0 or point[0]+upper_dx[index] >= lower[0] or point[1]+dy[index] < 0 or point[1]+dy[index] >= c:
            index += 1
        
        new_x = point[0]+upper_dx[index]
        new_y = point[1]+dy[index]

        if room[new_x][new_y] < 0:
            room[point[0]][point[1]] = 0
            break

        room[point[0]][point[1]] = room[new_x][new_y] 
        point = (new_x,new_y)

res = 0
for row in room:
    res += sum(row)

print(res+2)