import sys

MODULAR = 1000000007

def fast_pow(x, y):
    res = 1

    while y:
        if y%2:
            res = (res*x) % MODULAR
        y //= 2
        x = (x*x) % MODULAR

    return res

m = int(sys.stdin.readline().strip())
res = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    inv = fast_pow(a,MODULAR-2)
    res += (b*inv) % MODULAR

print(res%MODULAR)