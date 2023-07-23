#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
def check_triangle(sticks, i, j, k):
    if sticks[i] + sticks[j] <= sticks[k]:
        return False
    elif sticks[i] + sticks[k] <= sticks[j]:
        return False
    elif sticks[k] + sticks[j] <= sticks[i]:
        return False
    else:
        return True


def maximumPerimeterTriangle(sticks):
    perimeter, n = [[-1], 0], len(sticks)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if check_triangle(sticks, i, j, k):
                    per, coords = sticks[i] + sticks[j] + sticks[k], [sticks[i], sticks[j], sticks[k]]
                    if per > perimeter[-1]:
                        perimeter = [coords, per]
                    elif per == perimeter[-1]:
                        if max(perimeter[0]) < max(coords):
                            perimeter = [coords, per]
                        elif max(perimeter[0]) == max(coords):
                            if sorted(perimeter[0])[-1] < sorted(coords)[-1]:
                                perimeter = [coords, per]
    return sorted(perimeter[0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
