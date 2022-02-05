import sys

read = sys.stdin.readline

n = int(read().strip())
arr = sorted(map(int, read().split()))
x = int(read().strip())

left = 0
right = n-1
count = 0

while left < right and right < n:
    total = arr[left] + arr[right]

    if total < x:
        left += 1
    elif total > x:
        right -= 1
    else:
        count += 1
        left += 1

print(count)
        