def WayTooLongWords(n, arr):
    for i in range(n):
        if len(arr[i]) > 10:
            arr[i] = arr[i][0] + str(int(len(arr[i])-2)) + arr[i][-1]
    return arr



#TestCases only
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input().strip()
        arr.append(arr_item)
    result = WayTooLongWords(n, arr)
    for i in arr:
        print(i)