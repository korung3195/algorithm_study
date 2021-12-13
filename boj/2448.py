import sys

n = int(sys.stdin.readline().strip())

table = [[" " for _ in range(2*n-1)] for _ in range(n)]

table[0][n-1] = "*"
table[1][n-2] = "*"
table[1][n] = "*"
table[2][n-3] = "*"
table[2][n-2] = "*"
table[2][n-1] = "*"
table[2][n] = "*"
table[2][n+1] = "*"

def table_copy(table, n, start, end):
    step = end[0] - start[0] + 1
    for i in range(step):
        for j in range(2*step-1):
            table[step+i][n-j-2] = table[i][n+step-j-2]
            table[step+i][n+j] = table[i][n+step-j-2]

step = 3
while step < n:
    start = (0, n-step)
    end = (step-1, n+step-2)
    table_copy(table, n, start, end)

    step *= 2

for line in table:
    print("".join(line))



