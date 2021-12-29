import sys
sys.setrecursionlimit(10**6)

def getNext(grid, i, j, dir):
    if dir == 1:
        return (i-1, j) if i > 0 else (len(grid)-1, j)
    if dir == 2:
        return (i, j+1) if j < len(grid[0]) - 1 else (i, 0)
    if dir == 4:
        return (i+1, j) if i < len(grid) - 1 else (0, j)
    if dir == 8:
        return (i, j-1) if j > 0 else (i, len(grid[0])-1)

def getNextDir(dir_c, dir):
    if dir_c == "L":
        temp = dir >> 1
        return temp if temp > 0 else 8
    elif dir_c == "R":
        temp = dir << 1
        return temp if temp <= 15 else 1
    else:
        return dir

def isVisited(a, b):
    return a & b > 0

def search(grid, visited, i, j, dir, count):
    next_dir = getNextDir(grid[i][j], dir)
    if isVisited(visited[i][j], next_dir):
        return count
    visited[i][j] += next_dir
    next_i, next_j = getNext(grid, i, j, next_dir)
    return search(grid, visited, next_i, next_j, next_dir, count+1)

def solution(grid):
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    res = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dir = 1
            while dir <= 8:
                if isVisited(visited[i][j], dir):
                    dir *= 2
                    continue
                visited[i][j] += dir
                next_i, next_j = getNext(grid, i, j, dir)
                count = search(grid, visited, next_i, next_j, dir, 0)
                res.append(count+1)

    return sorted(res)