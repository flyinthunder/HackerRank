#!/bin/python3

import sys
import math


def prod(arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod


def mul_triplets(n):
    triplets = [[-1]]
    for i in range(n // 2):
        for j in range(n - i):
            if i ** 2 + j ** 2 == (n - (i + j)) ** 2:
                if i != 0 and j != 0:
                    triplets.append([i, j, (n - (i + j))])
    triplets = [prod(i) for i in triplets]
    return (max(triplets))


print(mul_triplets(1000))