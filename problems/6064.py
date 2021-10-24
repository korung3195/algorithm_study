import sys
import math

def solve():
    m,n,x,y = list(map(int,sys.stdin.readline().strip().split()))

    if m > n:
        temp_n, temp_y = m, x
        m, x = n, y
        n, y = temp_n, temp_y
    
    step = n-m
    temp = x

    for count in range(math.gcd(m,n)):
        if temp == y:
            return m*count+x
        temp = temp - step if temp + m > n else temp + m

    return -1

n = int(sys.stdin.readline().strip())

for _ in range(n):
    print(solve())