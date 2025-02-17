def allPossibleStrings(s):
    n = len(s)
    result = {}

    # Iterate through all subsets (represented by 0 to 2^n - 1)
    for i in range(1 << n):
        subset = ""
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset += s[j]

            # Add the subset to the result
        if subset in result.keys():
            result[subset] += 1
        else:
            result[subset] = 1

    return result

def calculate_fuction(s):
    if s == "":
        return 0
    else:
        last = s[0]
        partitions = 1
        for i in s[1:]:
            if i != last:
                partitions += 1
                last = i
            else:
                last = i
        return partitions


for _ in range(int(input().strip())):
    s = list(str(input().strip()))
    ops = int(input().strip())
    arr = list(map(int, input().strip().split()))
    output = []

    for i in arr:
        if s[i-1] == "1":
            s[i-1] = "0"
        elif s[i-1] == "0":
            s[i-1] = "1"

        total = 0
        d = allPossibleStrings("".join(s))
        for j in d.keys():
            total += calculate_fuction(j) * d[j]
        else:
            output.append(str(total))
    else:
        print(" ".join(output))