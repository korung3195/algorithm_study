from collections import deque

def solution(lines):
    queue = []
    window = deque()
    max_count = 0
    current_process = set()

    for i in range(len(lines)):
        line_split = lines[i].split()
        end = timeToStamp(line_split[1])
        start = int(end - (float(line_split[2][:-1])* 1000)) + 1
        
        queue.append((start, i))
        queue.append((end, i))

    queue.sort(reverse=True)
    while queue:
        stamp, index = queue.pop()

        if index not in current_process:
            current_process.add(index)
        else:
            window.append((stamp, index))

        while window and stamp - window[0][0] >= 1000:
            s, i = window.popleft()
            current_process.remove(i)
        
        max_count = max(max_count, len(current_process))

    return max_count

def timeToStamp(time):
    hour, minute, second = map(float, time.split(":"))
    return int((hour * 3600 + minute * 60 + second) * 1000)