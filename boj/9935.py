import sys
from collections import deque

string = sys.stdin.readline().strip()
exp_string = sys.stdin.readline().strip()
exp_length = len(exp_string)

stack = deque()

for s in string:
    flag = False
    stack.append(s)
    if stack[-1] == exp_string[-1]:
        flag = True
    while flag:
        if len(stack) < exp_length:
            break
        for i in range(exp_length):
            if stack[-i-1] != exp_string[-i-1]:
                flag = False
                break
        if flag:
            for i in range(exp_length):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")