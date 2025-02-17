testCases = int(input().strip())
for _ in range(testCases):
    n, m = map(int, input().strip().split())
    arr1, arr2 = list(map(int, input().strip().split())), list(map(int, input().strip().split()))
    arr2 = sorted(arr2)
    ans = "yes"
    if arr2[0] - arr1[0] < arr1[0]:
        last = arr2[0] - arr1[0]
        arr1[0] = last
    else:
        last = arr1[0]
    for i in range(1, n):
        arr = [arr2[j] - arr1[i] for j in range(m)]
        for j in range(len(arr)):
            if arr[j] <= arr1[i]:
                continue
            else:
                arr.insert(j, arr1[i])
        for j in arr:
            if j >= last:
                last = j
                arr1[i] = last
                break


    for j in range(n-1):
        if arr1[j] > arr1[j+1]:
            ans = "no"
    print(ans)
