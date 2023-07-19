#!/bin/python3

import sys

def fibb(n):
    a = 1
    b = 2
    sum = 2
    while a+b < n:
        if (a+b)%2==0:
            sum += a+b
        a,b = b,a+b
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibb(n))


# As we only need sum of even digits, no need to store any digits.
# n has values between 10 and 10^14 so we can start sum with 2