def solution(price, money, count):
    total = price * (count * (count+1)) // 2
    return max(0, total-money)