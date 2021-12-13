import sys

def read_int():
    return int(sys.stdin.readline().strip())

def solve():
    CURRENT_CHANNEL = 100
    n = read_int()
    m = read_int()
    broken = set(list(sys.stdin.readline().split())) if m > 0 else set()
    full_counts = abs(CURRENT_CHANNEL - n)

    if 98 <= n <= 103:
        return full_counts

    for i in range(full_counts):
        low = n-i
        high = n+i

        if 0<=low and not (set(list(str(low))) & broken):
            return min(i + len(str(low)), full_counts)
        if 0<=high and not (set(list(str(high))) & broken):
            return min(i + len(str(high)), full_counts)
        
    return full_counts

print(solve())