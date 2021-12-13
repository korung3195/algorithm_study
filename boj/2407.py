import sys

n,m = map(int,sys.stdin.readline().split())

def combination(n,m):
    if m > n//2:
        return combination(n, n-m)
    temp = 1
    for x in range(n,n-m,-1):
        temp *= x
    for y in range(m,0,-1):
        temp //= y 
    return temp

print(combination(n,m))