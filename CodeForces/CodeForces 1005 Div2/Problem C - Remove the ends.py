for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    while True:
        if arr[0] == 0:
            del arr[0]
        else:
            break

    while True:
        if arr[-1] == 0:
            del arr[-1]
        else:
            break
    pos_arr, neg_arr, temp_pos, temp_neg = [], [], [], []

    if arr[0] < 0:
        pos_arr.append(0)

    for i in arr:
        if i > 0:
            temp_pos.append(i)
            if sum(temp_neg) != 0:
                neg_arr.append(abs(sum(temp_neg)))
                temp_neg = []
        elif i < 0:
            temp_neg.append(i)
            if sum(temp_pos) != 0:
                pos_arr.append(sum(temp_pos))
                temp_pos = []
        elif i == 0:
            temp_pos.append(i)
            temp_neg.append(i)
    else:
        if sum(temp_pos) != 0:
            pos_arr.append(sum(temp_pos))
        if sum(temp_neg) != 0:
            neg_arr.append(abs(sum(temp_neg)))

    if arr[-1] > 0:
        neg_arr.append(0)
    temp_pos, temp_neg = [], []
    for i in pos_arr:
        if len(temp_pos) == 0:
            temp_pos.append(i)
        else:
            temp_pos.append(i + temp_pos[-1])
    else:
        pos_arr = temp_pos
    for i in neg_arr[::-1]:
        if len(temp_neg) == 0:
            temp_neg.append(i)
        else:
            temp_neg.append(i + temp_neg[-1])
    else:
        neg_arr = temp_neg[::-1]

    max = 0
    for i in range(len(pos_arr)):
        if pos_arr[i] + neg_arr[i] > max:
            max = pos_arr[i] + neg_arr[i]

    print(max)
