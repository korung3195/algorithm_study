import sys
from collections import deque

def op_D(x):
    return (x*2)%10000, "D"

def op_S(x):
    return x-1 if x>0 else 9999, "S"

def op_L(x):
    return (x%1000)*10+x//1000, "L"

def op_R(x):
    return (x%10)*1000+x//10, "R"

def transfer(before, after):
    visited = [False]*10001
    queue = deque()
    visited[before] = True
    queue.append(before)
    ops = [op_D,op_S,op_L,op_R]
    while queue:
        temp = queue.popleft()
        for op in ops:
            op_res, op_letter = op(temp)

            if op_res == after:
                res = op_letter
                track = temp
                while track != before:
                    res += visited[track][2]
                    track = visited[track][1]
                return res[::-1]

            if not visited[op_res]:
                visited[op_res] = [op_res, temp, op_letter]
                queue.append(op_res)

def solve():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        before, after = map(int,sys.stdin.readline().split())
        print(transfer(before, after))

solve()