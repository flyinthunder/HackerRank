for _ in range(int(input().strip())):
    n, q = map(int, input().strip().split(" "))
    slimes = list(map(int, input().strip().split(" ")))
    queries = [int(input().strip()) for i in range(q)]
    monotonus, scores = [], []
    for i in slimes:
        score = 0
        if len(monotonus) == 0:
            monotonus.append(i)
            scores.append(0)
        elif monotonus[-1] <= i:
            while len(monotonus) > 0 and monotonus[-1] <= i:
                del monotonus[-1]
                score += scores[-1] + 1
                del scores[-1]
            else:
                monotonus.append(i)
                scores.append(score)
        else:
            monotonus.append(i)
            scores.append(score)

    monotonus = monotonus[::-1]
    scores = scores[::-1]
    print(monotonus, scores, queries)

    for i in queries:
        score = 0
        for j in range(len(monotonus)):
            if i >= monotonus[j]:
                score += scores[j] + 1
        print(score)