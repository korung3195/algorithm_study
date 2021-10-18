import sys
import itertools

def readAndParseToList():
    return list(map(int, sys.stdin.readline().strip().split(' ')))

n, m = readAndParseToList()
numList = readAndParseToList()
accumulatedList = list(itertools.accumulate(numList))

for _ in range(m):
    start, end =  readAndParseToList()
    print(accumulatedList[end-1] - (accumulatedList[start-2]  if  start > 1 else 0))


