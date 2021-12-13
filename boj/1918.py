import sys

from collections import deque

stack = deque()
string = sys.stdin.readline().strip()
res = ""

for s in string:
    if s == "(":
        stack.append(s)
    elif s == ")":
        while stack[-1] != "(":
            res += stack.pop()
        stack.pop()
    elif s == "*" or s == "/":
        while stack and stack[-1] in ("*", "/"):
            res += stack.pop()
        stack.append(s)
    elif s == "+" or s == "-":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.append(s)
    else:
        res += s

while stack:
    res += stack.pop()

print(res)