def solution(line):
    length = len(line)
    points = set()

    min_x, min_y = 10**6, 10**6
    max_x, max_y = -10**6, -10**6

    for i in range(length):
        for j in range(i,length):
            A,B,E = line[i]
            C,D,F = line[j]

            factor = A*D - B*C

            if factor == 0:
                continue

            x = (B*F - E*D) / factor
            y = (E*C - A*F) / factor

            if x == int(x) and y == int(y):
                x, y = map(int, (x,y))
                points.add((x,y))
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)

    res = [["." for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]

    for x, y in points:
        res[max_y-y][x-min_x] = "*"

    return ["".join(row) for row in res]
