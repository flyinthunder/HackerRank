n, k = list(map(int, input().strip().split()))
scores = list(map(int, input().strip().split()))
winners = 0
for i in range(n):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        winners += 1
    else:
        break

print(winners)