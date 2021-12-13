import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

flag = s[0] == "I"
count = 0
temp = 0

for i in range(1, m):
    if flag:
        if(s[i] == s[i-1]):
            count += temp - n + 1 if temp >= n else 0
            temp = 0
            flag = False
        else:
            temp += 1 if s[i] == "I" else 0
    if s[i] == "I":
        flag = True

print(count + temp-n + 1 if flag and temp>=n else count)