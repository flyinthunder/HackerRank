#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    ret = "YES"
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j-1][i]:
                ret = "NO"
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        fptr.write(result + '\n')
    fptr.close()