import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
total = numbers[0]
min_length = n+1

while True:
    if left > right:
        right = left

    if total < s:
        right += 1
        if right > n-1:
            break
        total += numbers[right]
    elif total >= s:
        min_length = min(min_length, right-left+1)
        total -= numbers[left]
        left += 1
        if left > n-1:
            break
        
if min_length < n+1:
    print(min_length)
else:
    print(0)