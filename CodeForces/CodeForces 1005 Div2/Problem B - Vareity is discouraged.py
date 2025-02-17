for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    repeats, check = set([]), set([])
    for i in arr:
        if i in check:
            if i in repeats:
                continue
            else:
                repeats.add(i)
        else:
            check.add(i)

    start, end, max_len = -1, -1, -1
    t_start, t_end = -1, -1
    for i in range(len(arr)):
        if arr[i] not in repeats:
            if t_start == -1:
                t_start = i
            else:
                continue
        elif t_start != -1:
            t_end = i - 1
            if max_len < t_end - t_start:
                max_len = t_end - t_start
                start, end = t_start, t_end
                t_start, t_end = -1, -1
            else:
                t_start, t_end = -1, -1
        else:
            continue
    else:
        if t_start != -1:
            t_end = len(arr) - 1
            if max_len < t_end - t_start:
                max_len = t_end - t_start
                start, end = t_start, t_end
                t_start, t_end = -1, -1
    if start != -1:
        print(start+1, end+1)
    else:
        print(0)