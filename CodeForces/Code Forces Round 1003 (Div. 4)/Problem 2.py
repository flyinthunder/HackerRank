testCases = int(input().strip())
for i in range(testCases):
    ans = 1
    s = str(input().strip())
    current = s[0]
    for j in s[1:]:
        if j == current:
            ans = 1
            break
        else:
            ans += 1
            current = j
    print(ans)