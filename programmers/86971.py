def solution(n, wires):
    edges = dict()

    if n == 2:
        return 0

    for a, b in wires:
        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []

        edges[a].append(b)
        edges[b].append(a)
    
    min_diff = 100
    for a, b in wires:
        if len(edges[a]) == 1:
            a, b = b, a

        visited = [0] * (n+1)
        visited[a] = 1
        count = 1

        queue = set([edge for edge in edges[a] if edge != b])
        while queue:
            s = queue.pop()

            if visited[s]:
                continue

            count += 1
            visited[s] = 1

            for v in edges[s]:
                if v == a and s == b:
                    continue
                queue.add(v)

        min_diff = min(min_diff, abs(n-2 * count))

        if min_diff == n:
            break

    return min_diff
