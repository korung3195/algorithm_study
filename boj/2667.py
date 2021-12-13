import sys

n = int(sys.stdin.readline().strip())

queue = []
table = []
visited = [[0 for _ in range(n)] for _ in range(n)]
counts = []

for _ in range(n):
    table.append(list(map(int,list(sys.stdin.readline().strip()))))

for x in range(n):
    for y in range(n):
        if table[x][y] and not visited[x][y]:
            queue.append((x,y))
            count = 0
            while len(queue) > 0:
                (dest_x, dest_y) = queue.pop(0)

                if visited[dest_x][dest_y]:
                    continue

                visited[dest_x][dest_y] = 1
                count+=1

                if dest_x > 0 and table[dest_x-1][dest_y]:
                    queue.append((dest_x-1,dest_y))
                if dest_x < n-1 and table[dest_x+1][dest_y]:
                    queue.append((dest_x+1,dest_y))
                if dest_y > 0 and table[dest_x][dest_y-1]:
                    queue.append((dest_x,dest_y-1))
                if dest_y < n-1 and table[dest_x][dest_y+1]:
                    queue.append((dest_x,dest_y+1))

            counts.append(count)

counts.sort()
print(len(counts))
[print(x) for x in counts]