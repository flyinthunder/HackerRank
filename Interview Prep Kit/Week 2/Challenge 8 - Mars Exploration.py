#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    message = "SOS"
    errors = 0
    for i in range(len(s)):
        if s[i] != message[i%3]:
            errors += 1
    return errors

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()