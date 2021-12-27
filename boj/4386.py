import sys

def find(parents, target):
    while(parents[target] != target):
        target = parents[target]
    return target

def union(parents, target_a, target_b):
    parent_a = find(parents, target_a)
    parent_b = find(parents, target_b)
    
    if parent_a > parent_b:
        parents[parent_a] = parent_b
    else:
        parents[parent_b] = parent_a

n = int(sys.stdin.readline().strip())
points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]

edges = []

for i in range(n):
    for j in range(n):
        if i<=j:
            continue
        dist = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
        edges.append((dist, i, j))

edges.sort()

parents = [i for i in range(n)]
res = 0
count = 0
index = 0
while count < n-1:
    weight, start, end = edges[index]
    
    if find(parents, start) != find(parents, end):
        union(parents, start, end)
        res += weight
        count += 1

    index += 1

print(round(res,2))