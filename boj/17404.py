import sys

n = int(sys.stdin.readline().strip())

cost = [(0,0,0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
table = [(0,0,0) for _ in range(n+1)]

start = [(cost[1][0],1001,1001),(1001,cost[1][1],1001),(1001,1001,cost[1][2])]

min_res = 10**7

for c in range(3):
    cost[1] = start[c]
    for i in range(1,n+1):
        red = min(table[i-1][1], table[i-1][2]) + cost[i][0]
        green = min(table[i-1][0], table[i-1][2]) + cost[i][1]
        blue = min(table[i-1][0], table[i-1][1]) + cost[i][2]
        table[i] = (red, green, blue)
    
    for j in range(3):
        if c==j:
            continue
        if table[n][j] < min_res:
            min_res = table[n][j]

print(min_res)