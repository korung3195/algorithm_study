import sys

n = int(sys.stdin.readline().strip())
table = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    temp = [False] * n
    for j in range(n):
        if not row[j]:
            temp[j] = [0,0,0]
    table.append(temp)

table[0][0] = False
table[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if not table[i][j]:
            continue
        if j > 0 and table[i][j-1]:
            table[i][j][0] = table[i][j-1][0] + table[i][j-1][1]
        if j > 0 and i > 0 and table[i][j-1] and table[i-1][j] and table[i-1][j-1]:
            table[i][j][1] = table[i-1][j-1][0] + table[i-1][j-1][1] + table[i-1][j-1][2]
        if i > 0 and table[i-1][j]:
            table[i][j][2] = table[i-1][j][1] + table[i-1][j][2]

if not table[n-1][n-1]:
    print(0)
else:
    print(sum(table[n-1][n-1]))