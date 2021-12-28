import sys

def solve():
    n = int(sys.stdin.readline().strip())
    sqrt_n = int(n**0.5)

    if n==1:
        print(0)
        return

    table = [True for _ in range(n+1)]
    table[0] = False
    table[1] = False

    for i in range(sqrt_n+1):
        if not table[i]:
            continue
        mult = 2
        while mult * i <= n:
            table[mult * i] = False
            mult += 1

    primes = [i for i in range(1, n+1) if table[i]]

    left = 0
    right = 0
    temp_sum = primes[0]
    count = 0

    while True:
        if temp_sum > n:
            temp_sum -= primes[left]
            left += 1
            continue

        if temp_sum == n:
            count += 1
        right += 1

        if right >= len(primes):
            break

        temp_sum += primes[right]

    print(count)

solve()