n,m = input().split(" ")
myDict = dict();

for _ in range(int(n)):
    domain, password = input().split(" ")
    myDict[domain] = password

for _ in range(int(m)):
    domain = input()
    print(myDict[domain])