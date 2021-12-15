def solution(key, lock):
    n = len(lock)
    m = len(key)
    count = n**2 - sum([sum(line) for line in lock])
    blank = [0] * (2*m+n-2)
    lock = [blank]*(m-1) + [[0]*(m-1) + line + [0]*(m-1) for line in lock] + [blank]*(m-1)

    for _ in range(4):
        key = rotate(key, m)
        for i in range(n+m-1):
            for j in range(n+m-1):
                if check(key, lock, m, n, i, j, count):
                    return True
    return False

def check(key, lock, m, n, i, j, count):
    for x in range(m):
        for y in range(m):
            if key[x][y] + lock[i+x][j+y] > 1:
                return False
            if m-1<=i+x<m+n-1 and m-1<=j+y<m+n-1 and key[x][y] == 1 and lock[i+x][j+y] == 0:
                count -= 1
    return count == 0

def rotate(key, m):
    res = []
    for i in range(m):
        temp = []
        for j in range(m):
            temp.append(key[m-j-1][i])
        res.append(temp)
    return res