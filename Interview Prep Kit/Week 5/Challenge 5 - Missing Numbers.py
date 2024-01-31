#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    missing_no = []
    acount = {}
    bcount = {}
    for i in arr:
        if i in acount.keys():
            acount[i] += 1
        else:
            acount[i] = 1

    for i in brr:
        if i in bcount.keys():
            bcount[i] += 1
        else:
            bcount[i] = 1

    for i in bcount.keys():
        if i in acount.keys() and bcount[i] == acount[i]:
            pass
        else:
            missing_no.append(i)

    return sorted(missing_no)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
