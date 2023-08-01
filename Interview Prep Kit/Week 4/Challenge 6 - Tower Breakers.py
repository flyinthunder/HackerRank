#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if n%2 == 0 or m == 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()


#If number of towers is even, p2 always wins by simply mirroing player 1
#if number of towers is odd, p1 always wins by reducing one tower to 1 and mirroring player 2
#if towers start at a height of 1, p1 loses immidiately