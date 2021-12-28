import sys

read = sys.stdin.readline

t = int(read().strip())
n = int(read().strip())
arr_n = list(map(int, read().split()))
m = int(read().strip())
arr_m = list(map(int, read().split()))

sum_dict = dict()

for i in range(n):
    temp_sum = 0
    for j in range(i,n):
        temp_sum += arr_n[j]

        if temp_sum in sum_dict:
            sum_dict[temp_sum] += 1
        else:
            sum_dict[temp_sum] = 1

count = 0
for i in range(m):
    temp_sum = 0
    for j in range(i, m):
        temp_sum += arr_m[j]
        
        diff = t-temp_sum
        if diff in sum_dict:
            count += sum_dict[diff]

print(count)