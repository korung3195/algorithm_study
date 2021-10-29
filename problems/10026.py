import sys
from collections import deque

n = int(sys.stdin.readline().strip())
table = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited_three_color = [[0 for _ in range(n)] for _ in range(n)]
visited_two_color = [[0 for _ in range(n)] for _ in range(n)]
queue_three_color = deque()
queue_two_color = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count_three_color = 0
count_two_color = 0
similar_color = ["R","G"]

for i in range(n):
    for j in range(n):
        if not visited_three_color[i][j]:
            visited_three_color[i][j] = 1
            queue_three_color.append((i,j))
            count_three_color += 1

        if not visited_two_color[i][j]:
            visited_two_color[i][j] = 1
            queue_two_color.append((i,j))
            count_two_color += 1
        
        while queue_three_color:
            x,y = queue_three_color.popleft()
            color = table[x][y]
            for k in range(4):
                new_x = x+dx[k]
                new_y = y+dy[k]
                isValidPoint = 0<=new_x<n and 0<=new_y<n
                isSameColor = isValidPoint and color == table[new_x][new_y]
                if isSameColor and not visited_three_color[new_x][new_y]:
                    visited_three_color[new_x][new_y] = 1
                    queue_three_color.append((new_x,new_y))

        while queue_two_color:
            x,y = queue_two_color.popleft()
            color = table[x][y]
            for k in range(4):
                new_x = x+dx[k]
                new_y = y+dy[k]
                isValidPoint = 0<=new_x<n and 0<=new_y<n
                isSameColor = isValidPoint and (color == table[new_x][new_y] or (color in similar_color and table[new_x][new_y] in similar_color))
                if isSameColor and not visited_two_color[new_x][new_y]:
                    visited_two_color[new_x][new_y] = 1
                    queue_two_color.append((new_x,new_y))

print(count_three_color, count_two_color)