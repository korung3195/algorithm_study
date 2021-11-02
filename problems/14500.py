import sys

def readInt():
    return map(int, sys.stdin.readline().split())

n, m = readInt()
table = [list(readInt()) for _ in range(n)]

res = 0

for i in range(n):
    for j in range(m):
        if j <= m-4:
            res = max(res, sum([table[i][j],table[i][j+1],table[i][j+2],table[i][j+3]]))
        if j <= m-3 and i <= n-2:
            res = max(res, sum([table[i][j],table[i][j+1],table[i][j+2],table[i+1][j]]))
            res = max(res, sum([table[i][j],table[i][j+1],table[i][j+2],table[i+1][j+1]]))
            res = max(res, sum([table[i][j],table[i][j+1],table[i][j+2],table[i+1][j+2]]))
            res = max(res, sum([table[i][j],table[i][j+1],table[i+1][j+1],table[i+1][j+2]]))
            res = max(res, sum([table[i][j],table[i+1][j],table[i+1][j+1],table[i+1][j+2]]))
            res = max(res, sum([table[i][j+1],table[i+1][j],table[i+1][j+1],table[i+1][j+2]]))
            res = max(res, sum([table[i][j+2],table[i+1][j],table[i+1][j+1],table[i+1][j+2]]))
            res = max(res, sum([table[i][j+2],table[i+1][j],table[i+1][j+1],table[i][j+1]]))
        if j <= m-2 and i <= n-2:
            res = max(res, sum([table[i][j],table[i][j+1],table[i+1][j],table[i+1][j+1]]))
        if j <= m-2 and i <= n-3:
            res = max(res, sum([table[i][j],table[i][j+1],table[i+1][j+1],table[i+2][j+1]]))
            res = max(res, sum([table[i][j],table[i+1][j],table[i+1][j+1],table[i+2][j+1]]))
            res = max(res, sum([table[i][j],table[i+1][j],table[i+2][j],table[i+2][j+1]]))
            res = max(res, sum([table[i][j],table[i+1][j],table[i+1][j+1],table[i+2][j]]))
            res = max(res, sum([table[i][j],table[i][j+1],table[i+1][j],table[i+2][j]]))
            res = max(res, sum([table[i+1][j],table[i][j+1],table[i+1][j+1],table[i+2][j+1]]))
            res = max(res, sum([table[i+2][j],table[i][j+1],table[i+1][j+1],table[i+2][j+1]]))
            res = max(res, sum([table[i+2][j],table[i][j+1],table[i+1][j+1],table[i+2][j+1]]))
            res = max(res, sum([table[i+2][j],table[i][j+1],table[i+1][j+1],table[i+1][j]]))
        if i <= n-4:
            res = max(res, sum([table[i][j],table[i+1][j],table[i+2][j],table[i+3][j]]))

print(res)