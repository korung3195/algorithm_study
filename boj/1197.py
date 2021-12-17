import sys

def find(parents, target):
    while parents[target] != target:
        target = parents[target]
    return target

def union(parents, a, b):
    parent_a = find(parents, a)
    parent_b = find(parents, b)
    if parent_a > parent_b:
        parents[parent_a] = parent_b
    else:
        parents[parent_b] = parent_a

v, e = map(int, sys.stdin.readline().split())
edges = []
parents = [i for i in range(v+1)]
visited = set()

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()
count = 0
res = 0

for c,a,b in edges:
    if find(parents, a) != find(parents, b):
        count += 1
        union(parents, a, b)
        res += c

    if count == v-1:
        break

print(res)