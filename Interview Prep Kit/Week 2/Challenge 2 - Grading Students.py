#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            pass
        elif str(grades[i]).endswith("3") or str(grades[i]).endswith("4"):
            grades[i] = int((grades[i]//10)*10 + 5)
        elif str(grades[i]).endswith("8") or str(grades[i]).endswith("9"):
            grades[i] = int((grades[i]//10)*10 + 10)
        else:
            pass
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
