import sys

n = int(sys.stdin.readline().strip())
table = []

for _ in range(n):
    size = int(sys.stdin.readline().strip())
    table = []
    dp = [[0 for _ in range(size)] for _ in range(2)]

    for _ in range(2):
        table.append(list(map(int,sys.stdin.readline().split())))
    
    dp[0][0]=table[0][0]
    dp[1][0]=table[1][0]

    if size > 1:
        dp[0][1]=table[1][0]+table[0][1]
        dp[1][1]=table[0][0]+table[1][1]

    for i in range(2, size):
        dp[0][i] = table[0][i]+max(dp[1][i-1],dp[1][i-2])
        dp[1][i] = table[1][i]+max(dp[0][i-1],dp[0][i-2])
    
    print(max(dp[0][size-1],dp[1][size-1]))