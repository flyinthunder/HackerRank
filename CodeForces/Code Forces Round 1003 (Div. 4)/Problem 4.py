def score(a, y):
    ans = 0
    for x in a:
        ans += x*y
        y -= 1
    return ans

for _ in range(int(input().strip())):
    total = 0
    n, m = map(int, input().strip().split())
    arr, weights, scores = [], [], []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
        weights.append(sum(arr[-1]))
        scores.append(score(arr[-1], m))
    weights, scores = zip(*sorted(zip(weights, scores), reverse=True))
    mul = m*(n-1)
    for i in range(n):
        total += weights[i] * mul + scores[i]
        mul -= m
    print(total)