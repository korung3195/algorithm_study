import sys

n = int(sys.stdin.readline().strip())
arr = [1, 3]

for i in range(2, n):
    arr.append(arr[i-1] + arr[i-2] * 2) 

print(arr[n-1] % 10007)