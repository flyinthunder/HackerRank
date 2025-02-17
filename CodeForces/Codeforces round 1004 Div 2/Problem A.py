for _ in range(int(input().strip())):
    n, m = map(int, input().strip().split())
    arr = []
    mul = n//9
    for i in range(mul+1):
        if m == (((n%9)+1)+9*i):
            print("yes")
            break
    else:
        print("no")