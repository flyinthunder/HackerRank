#!/bin/python3

import sys
import math

def mul_triplets(n):
    max_triplets = -1
    for i in range(n//3):
        j = (n**2 - 2*i*n)//(2*n - 2*i)
        k = n - i - j
        if i**2 + j**2 == k**2:
            if i*j*k > max_triplets and i*j*k != 0:
                max_triplets = i*j*k
    return max_triplets

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(mul_triplets(n))

# Only iterate over given array once as
# double iteration causes timeout.