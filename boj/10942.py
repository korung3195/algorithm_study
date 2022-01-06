import sys

read = sys.stdin.readline

n = int(read().strip())
numbers = list(map(int, read().split()))
m = int(read().strip())

table = [[0 for _ in range(n+1)] for _ in range(n+1)]

index = 1
x = 1
y = 1

while index <= n:
    if x == y or numbers[x-1] == numbers[y-1] and (x+1 > y-1 or table[x+1][y-1]):
        table[x][y] = 1

    x += 1
    y += 1
    if y > n:
        index += 1
        x = 1
        y = index

for _ in range(m):
    s, e = map(int, read().split())
    print(table[s][e])