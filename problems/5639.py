import sys
sys.setrecursionlimit(10**6)
        
arr = []

def recur(start, end):
    if start == end:
        print(arr[start])
        return
    elif start > end:
        return

    for i in range(start+1, end+1):
        if arr[i] > arr[start]:
            recur(start+1,i-1)
            recur(i, end)
            print(arr[start])
            return

    recur(start+1, end)
    print(arr[start])

while True:
    try:
        arr.append(int(sys.stdin.readline().strip()))
    except:
        break;

recur(0, len(arr)-1)