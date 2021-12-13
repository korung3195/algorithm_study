import sys

n = int(sys.stdin.readline().strip())
table = [[(0,0),(0,0),(0,0)] for _ in range(2)]

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    index = i%2
    prev_index = 1-index

    table[index][0] = (min(table[prev_index][0][0], table[prev_index][1][0])+a, max(table[prev_index][0][1], table[prev_index][1][1])+a)
    table[index][1] = (min(table[prev_index][0][0], table[prev_index][1][0], table[prev_index][2][0])+b, max(table[prev_index][0][1], table[prev_index][1][1], table[prev_index][2][1])+b)
    table[index][2] = (min(table[prev_index][1][0], table[prev_index][2][0])+c, max(table[prev_index][1][1], table[prev_index][2][1])+c)

res = table[1-n%2]
print(max([tup[1] for tup in res]), min([tup[0] for tup in res]))