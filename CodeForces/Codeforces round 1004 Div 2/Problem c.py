for _ in range(int(input().strip())):
    n = int(input().strip())
    if "7" in str(n):
        print("0")
        continue
    lenn = len(str(n)) + 1
    arr = []
    for i in range(lenn):
        arr.append(int("9"*(i+1)))
    bp = False
    for i in range(8):
        for j in arr:
            if "7" in str(n + j):
                print(i+1)
                bp = True
                break
            else:
                continue
        else:
            t = []
            k = 9
            for j in arr:
                t.append(j+k)
                k = k*10 + 9
            arr = t
        if bp:
            break
