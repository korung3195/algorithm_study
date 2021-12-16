import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

table = [[0 for _ in range(len(first)+1)] for _ in range(len(second)+1)]

for i in range(1, len(second)+1):
    for j in range(1, len(first)+1):
        if second[i-1] == first[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

i = len(second)
j = len(first)
res = []

while i > 0 and j > 0:
    if table[i-1][j] == table[i][j]:
        i -= 1
    elif table[i][j-1] == table[i][j]:
        j -= 1
    else:
        res.append(first[j-1])
        i -= 1
        j -= 1

count = len(res)
print(count)

if count > 0:
    print("".join(res[::-1]))