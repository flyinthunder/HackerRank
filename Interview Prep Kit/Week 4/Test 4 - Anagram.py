#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s)%2 == 1:
        return -1
    s1, s2 = s[0:(len(s)//2)], s[len(s)//2:len(s)]
    diff = [0 for i in range(26)]
    for i in range(len(s1)):
        diff[ord(s1[i])-97] += 1
        diff[ord(s2[i])-97] -= 1
    sum = 0
    for i in diff:
        if i >= 0:
            sum += i
        elif i < 0:
            pass
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')
    fptr.close()