import sys

n = int(sys.stdin.readline().strip())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        for z in range(n):
            if table[y][x] and table[x][z]:
                table[y][z] = 1

for row in table:
    print(*row,sep=" ")