import sys

n = int(sys.stdin.readline().strip())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.append(points[0])

temp1 = 0
temp2 = 0
for i in range(len(points)-1):
    temp1 += points[i][0] * points[i+1][1]
    temp2 += points[i][1] * points[i+1][0]

print(0.5*abs(temp1-temp2))