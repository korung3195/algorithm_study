import sys

def find(table, target):
    while table[target] != target:
        target = table[target]
    return target

def union(table, target_a, target_b):
    parent_a = find(table, target_a)
    parent_b = find(table, target_b)
    if parent_a < parent_b:
        table[parent_a] = parent_b
    else:
        table[parent_b] = parent_a

n, m = map(int ,sys.stdin.readline().split())
edges = []
table = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int ,sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()

res = 0
count = 0
for c,a,b in edges:
    if count == n-2:
        break
    if find(table, a) != find(table, b):
        union(table, a, b)
        res += c
        count += 1

print(res)