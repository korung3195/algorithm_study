import sys

read = sys.stdin.readline

t = int(read().strip())

def solve():
    n = int(read().strip())
    selected = [0] + list(map(int, read().split()))
    visited = [0] * (n+1)
    cycled = [False] * (n+1)
    count = 0

    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = i
        next = selected[i]

        while not visited[next]:
            visited[next] = i
            next = selected[next]
        
        if cycled[next] or visited[next] != i:
            continue
        
        while not cycled[next]:
            count += 1
            cycled[next] = True
            next = selected[next]

    print(n-count)
    
for _ in range(t):
    solve()