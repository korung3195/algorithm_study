import sys, heapq

n, m = map(int, sys.stdin.readline().split())

dist = [float('inf')] * 100001
dist[n] = 0

queue = [(0,n)]

while queue:
    weight, now = heapq.heappop(queue)

    if dist[now] < weight:
        print(dist[now], weight)
        continue

    if now == m:
        break

    if now <= 50000 and dist[2*now] > weight:
        dist[2*now] = weight
        heapq.heappush(queue,(weight,2*now))
    
    if now > 0 and dist[now-1] > weight + 1:
        dist[now-1] = weight+1
        heapq.heappush(queue,(weight+1,now-1))

    if now < 100000 and dist[now+1] > weight + 1:
        dist[now+1] = weight+1
        heapq.heappush(queue,(weight+1,now+1))

print(dist[m])