def solution(n, t, m, timetable):
    timetable = sorted(map(timeToHour,timetable), reverse=True)
    max_time = 0

    time = 540
    while n > 0:
        count = 0
        while count < m and timetable and timetable[-1] <= time:
            victim = timetable.pop()
            count += 1
            if count == m:
                max_time = victim - 1
        if count < m:
            max_time = time
        n -= 1
        time += t

    return hourToTime(max_time)

def timeToHour(time):
    hour, minute = map(int,time.split(":"))
    return hour*60+minute

def hourToTime(hour):
    return str(hour//60).zfill(2) + ":" + str(hour%60).zfill(2)