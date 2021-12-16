import sys

n = int(sys.stdin.readline().strip())
table = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(table)-1
temp = (0, 0)
min_diff = 10**10

while left < right:
    diff = table[left] + table[right]
    if min_diff > abs(diff):
        temp = (table[left], table[right])
        min_diff = abs(diff)
    if diff < 0:
        left += 1
    elif diff > 0:
        right -= 1
    else:
        break

print(*temp)