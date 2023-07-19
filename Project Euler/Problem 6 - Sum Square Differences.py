#!/bin/python3

import sys

def sum_square_differences(n):
    sum_squares = 0
    for i in range(n+1):
        sum_squares += i**2
    return ((n*(n+1)//2)**2) - sum_squares

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_square_differences(n))

# for given number n,
# return (1+2+3...n)^2 - (1^2 + 2^2 ... n^2)
#        (n*n+1/2)^2 - ...
