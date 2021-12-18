import sys

def solve():
    n = int(sys.stdin.readline().strip())
    table = sorted(map(int, sys.stdin.readline().split()))

    min_diff = 10**10
    res = (0,0,0)

    for i in range(n-2):
        fixed = table[i]
        left = i+1
        right = n-1
        
        while left < right:
            temp_sum = fixed + table[left] + table[right]

            if abs(temp_sum) < min_diff:
                min_diff = min(abs(temp_sum), min_diff)
                res = (fixed, table[left], table[right])

            if temp_sum < 0:
                left += 1
            elif temp_sum > 0:
                right -= 1
            else:
                return res
    
    return res

print(*solve())
                