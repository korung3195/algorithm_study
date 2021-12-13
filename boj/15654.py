import sys

n, m = map(int, sys.stdin.readline().split())
table = list(map(int, sys.stdin.readline().split()))
table.sort()
visited = [0] * n

def track(count, memo):
    if(count == 0):
        print(memo.strip())
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            track(count-1, memo + str(table[i]) + " ")
            visited[i] = 0

track(m, "")