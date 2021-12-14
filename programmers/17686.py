def solution(files):
    res = []
    for file in files:
        index = -1
        temp = []

        for i in range(len(file)):
            if index < 0 and file[i].isdigit():
                index = i
                temp.append(file[:index])
            elif index > 0 and not file[i].isdigit():    
                temp.append(file[index:i])
                temp.append(file[i:])
                break
        if len(temp) < 2:
            temp.append(file[index:])
        res.append(temp)

    res.sort(key = lambda x: (x[0].lower(),int(x[1])))
    return ["".join(file) for file in res]