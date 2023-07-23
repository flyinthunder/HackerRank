#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def change_level(level, i):
    if i == "D":
        level -= 1
        return level
    if i == "U":
        level += 1
        return level


def countingValleys(steps, path):
    valleys = 0
    level = 0
    for i in path:
        level = change_level(level, i)
        if i == "U" and level == 0:
            valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()