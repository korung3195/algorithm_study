import sys
from collections import deque

def solve():
    n, m = map(int,sys.stdin.readline().split())

    visited = [0 for i in range(101)]
    ladder_snake_map = [0 for i in range(101)]

    for _ in range(n+m):
        start, end = map(int,sys.stdin.readline().split())
        ladder_snake_map[start] = end

    queue = deque()
    queue.append(1)
    visited[1] = 1
    count = 0

    while queue:
        length = len(queue)
        count += 1
        for _ in range(length):
            start = queue.popleft()
            for i in range(1,7):
                if start+i == 100:
                    return count
                if visited[start+i]:
                    continue

                visited[start+i] = 1
                ladder_snake_dest = ladder_snake_map[start+i]
                if ladder_snake_dest and not visited[ladder_snake_dest]:
                    visited[ladder_snake_dest] = 1
                    queue.append(ladder_snake_dest)
                elif not ladder_snake_dest:
                    queue.append(start+i)

print(solve())