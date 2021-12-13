import sys, heapq

INF = 10**8
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

dist_table = [INF] * (n+1)
bus_table = dict()

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    if start in bus_table:
        if end in bus_table[start]:
            bus_table[start][end] = min(bus_table[start][end], weight)
        else:
            bus_table[start][end] = weight
    else:
        bus_table[start] = dict({end:weight})

dest_start, dest_end = map(int, sys.stdin.readline().split())

dist_table[dest_start] = 0
queue = [(0, dest_start)]

while queue:
    weight, pos = heapq.heappop(queue)

    if weight > dist_table[pos]:
        continue

    if not pos in bus_table:
        continue

    for v in bus_table[pos]:
        if dist_table[v] > weight + bus_table[pos][v]:
            dist_table[v] = weight + bus_table[pos][v]
            heapq.heappush(queue, (dist_table[v], v))

print(dist_table[dest_end])