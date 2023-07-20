#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s = s.split(":")
    if s[0] == "12":
        s[0] = "00"
    if s[-1].endswith("PM"):
        s[0] = str(int(s[0]) + 12)
        if len(s[0]) == 1:
            s[0] = "0" + s[0]
    s[-1] = s[-1][:-2]
    return ":".join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
