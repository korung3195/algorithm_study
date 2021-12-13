def solution(msg):
    res = []
    dic = dict()
    base = ord("A")

    for c in range(base, ord("Z")+1):
        dic[chr(c)] = c-base+1

    count = 27
    index = 0
    temp = ""
    while index < len(msg):
        temp = msg[index]
        index += 1

        while True:
            if index >= len(msg):
                break
            temp += msg[index]
            if temp not in dic:
                break
            index += 1

        if temp not in dic:
            dic[temp] = count
            count += 1

        if len(temp) > 1 and index < len(msg):
            res.append(dic[temp[:-1]])
        else:
            res.append(dic[temp])

    return res