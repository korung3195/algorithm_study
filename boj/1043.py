import sys

n, m = map(int, sys.stdin.readline().split())
line = list(map(int, sys.stdin.readline().split()))

party_list = []
people_with_truth = set(line[1:])

for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    party_list.append(set(temp[1:]))

flag = True
while flag:
    flag = False
    for i in range(m):
        if party_list[i] and party_list[i].intersection(people_with_truth):
            people_with_truth = party_list[i].union(people_with_truth)
            party_list[i] = False
            flag = True

print(m-sum([1 for x in party_list if not x]))