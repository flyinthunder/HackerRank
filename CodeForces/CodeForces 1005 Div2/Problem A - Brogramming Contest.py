for _ in range(int(input().strip())):
    n = int(input().strip())
    s = list(str(input().strip()))
    new_s = []
    for i in range(len(s)):
        if i == 0 and s[i] == "0":
            continue
        elif i==0 and s[i] == "1":
            new_s.append(s[i])
        elif s[i] == s[i-1]:
            continue
        else:
            new_s.append(s[i])
    print(len(new_s))