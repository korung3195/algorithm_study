def solution(n, left, right):
    res = []
    
    for i in range(int(left), int(right)+1):
        x = i // n
        y = i % n
        res.append(max(x,y)+1)
    
    return res