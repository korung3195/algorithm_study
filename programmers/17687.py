def solution(n, t, m, p):
    res = []
    count = 0
    left = 0
    num = 0

    while count < t:
        temp = transfer(num, n)
        for i in range(len(temp)):
            if (i+left) % m == p-1:
                res.append(temp[i])
                count += 1
            if count >= t:
                return "".join(res)
        num += 1
        left = (len(temp)+left)%m

    return res

def transfer(num, base):
    res = []
    if num == 0:
        return "0"

    while num > 0:
        char = str(num%base) if num%base < 10 else chr(ord('A') + (num%base-10))
        res.append(char)
        num //= base
    return "".join(res[::-1])
