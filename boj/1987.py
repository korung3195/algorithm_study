import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

queue = set([(0,0,board[0][0])])
max_length = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y, visited = queue.pop()
    max_length = max(max_length, len(visited))

    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
            continue

        point = board[new_x][new_y]
        if point not in visited:
            queue.add((new_x, new_y, visited+point))

print(max_length)