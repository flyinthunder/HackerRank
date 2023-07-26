#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
def split(s, num_len):
    splt = []
    i = 0
    while i < len(s):
        if len(s) <= i + num_len:
            splt.append(s[i:])
            return splt
        splt.append(s[i:i + num_len])
        inc = True
        for j in s[i:i + num_len]:
            if j != "9":
                inc = False
        if inc:
            i += num_len
            num_len += 1
        else:
            i += num_len
    return splt


def separateNumbers(s):
    for num_len in range(1, (len(s) // 2) + 1):
        splt = split(s, num_len)
        beautiful = True
        for i in range(len(splt) - 1):
            if int(splt[i]) + 1 != int(splt[i + 1]):
                beautiful = False
            if splt[i][0] == "0":
                beautiful = False
        if beautiful:
            return "YES " + splt[0]
    return "NO"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        print(separateNumbers(s))
