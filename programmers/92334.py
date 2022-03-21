def solution(id_list, report, k):
    number = len(id_list)
    nameToIndex = dict()
    reports = [set() for _ in range(number)]
    report_count = [0] * number
    answer = [0] * number

    for i in range(number):
        nameToIndex[id_list[i]] = i
    
    for s in report:
        reporter, reportee = map(nameToIndex.get, s.split(" "))
    
        if reportee not in reports[reporter]:
            report_count[reportee] += 1
            reports[reporter].add(reportee)
    
    for i in range(number):
        count = 0
        for r in reports[i]:
            if report_count[r] >= k:
                count += 1

        answer[i] = count

    return answer