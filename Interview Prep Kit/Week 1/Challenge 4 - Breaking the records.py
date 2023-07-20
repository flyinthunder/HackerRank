#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_rec, min_score = 0, scores[0]
    max_rec, max_score = 0, scores[0]
    for i in scores:
        if i < min_score:
            min_rec += 1
            min_score = i
        if i > max_score:
            max_rec += 1
            max_score = i
    return [max_rec, min_rec]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()