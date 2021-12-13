def time_diff(time_a, time_b):
    hour_a, min_a = map(int, time_a.split(":"))
    hour_b, min_b = map(int, time_b.split(":"))

    min_a += hour_a*60 
    min_b += hour_b*60

    return min_b - min_a

def transfer(song):
    res = ""
    for i in range(len(song)):
        if song[i]=="#":
            continue
        elif i < len(song)-1 and song[i+1] == "#":
            res += song[i].lower()
        else:
            res += song[i]
    return res

def solution(m, musicinfos):
    m = transfer(m)
    temp = []

    for info in musicinfos:
        split_info = info.split(",")
        minute = time_diff(split_info[0], split_info[1])
        name = split_info[2]
        song = transfer(split_info[3])
        song_length = len(song)

        index = 0
        for i in range(minute):
            if song[i%song_length] != m[index]:
                index = 0
                continue
            index += 1
            if index >= len(m):
                temp.append((minute, name))
                break
    
    max_minute = 0
    max_name = "(None)"
    for minute, name in temp:
        if max_minute < minute:
            max_minute = minute
            max_name = name

    return max_name