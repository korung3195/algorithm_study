import sys

read = sys.stdin.readline

def solve():
    MAX_COST = 100
    n, m = map(int, read().split())
    memory = [-1] + list(map(int, read().split()))
    cost = [-1] + list(map(int, read().split()))

    table = [[0 for _ in range(n*MAX_COST+1)] for _ in range(n+1)]
    min_cost = n * MAX_COST + 1

    for i in range(1, n+1):
        for j in range(n*MAX_COST+1):
            c = cost[i]
            if c <= j and table[i-1][j] < table[i-1][j-c] + memory[i]:
                table[i][j] = table[i-1][j-c] + memory[i]
                if table[i][j] >= m:
                    min_cost = min(j, min_cost)
            else:
                table[i][j] = table[i-1][j]

    return min_cost
                    

print(solve())