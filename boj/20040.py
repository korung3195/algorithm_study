import sys

def intRead():
    return map(int, sys.stdin.readline().split())

def find(parents, target):
    while parents[target] != target:
        target = parents[target]
    return target

def solve():
    n, m = intRead()

    parents = [i for i in range(n)]

    for i in range(1,m+1):
        a, b = intRead()

        parent_a = find(parents, a)
        parent_b = find(parents, b)

        if parent_a == parent_b:
            return i

        if parent_a > parent_b:
            parents[parent_a] = parent_b
        else:
            parents[parent_b] = parent_a

    return 0

print(solve())
