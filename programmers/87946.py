from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for permut in permutations(dungeons):
        count = 0
        left_cost = k
        for min_cost, cost in permut:
            if min_cost > left_cost:
                break
            left_cost -= cost
            count += 1
        max_count = max(max_count, count)
            
    return max_count

print(solution(80, [[80,20],[50,40],[30,10]]))