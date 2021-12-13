import sys

n, m = map(int,sys.stdin.readline().split())

table = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    res = [0] * n
    for j in range(n):
        if j>=1:
            temp[j] = temp[j] + temp[j-1]
        res[j] = temp[j] + (table[i-1][j] if i>=1 else 0)
    table.append(res)

for _ in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    print(table[x2-1][y2-1] - (table[x2-1][y1-2] if y1>1 else 0) - (table[x1-2][y2-1] if x1>1 else 0) + (table[x1-2][y1-2] if x1>1 and y1>1 else 0))