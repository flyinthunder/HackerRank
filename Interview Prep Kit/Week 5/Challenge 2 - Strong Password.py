#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

class Password():
    def __init__(self, password):
        self.password = password
        self.strong, self.addnumber = self.is_strong()

    def has_lower(self):
        for i in self.password:
            if i.islower():
                return True
        return False

    def has_upper(self):
        for i in self.password:
            if i.isupper():
                return True
        return False

    def has_number(self):
        number = "0123456789"
        for i in self.password:
            if i in number:
                return True
        return False

    def has_special(self):
        special = "!@#$%^&*()-+"
        for i in self.password:
            if i in special:
                return True
        return False

    def is_strong(self):
        length = len(self.password)
        min_chars = 0
        if not self.has_lower():
            min_chars += 1
        if not self.has_upper():
            min_chars += 1
        if not self.has_number():
            min_chars += 1
        if not self.has_special():
            min_chars += 1
        if min_chars == 0 and length >= 6:
            return True, 0
        elif min_chars > 0 and length + min_chars >= 6:
            return False, min_chars
        else:
            return False, 6 - length


def minimumNumber(n, password):
    p = Password(password)
    return p.addnumber


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()