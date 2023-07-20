#!/bin/python3

import sys


def prod(arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod


def multiply(n, k):
    numbers = []
    for i in range(len(str(n)) - k):
        numbers.append([int(i) for i in [*str(n)[i:i + k]]])
    mult = [int(prod(i)) for i in numbers]
    return max(mult)


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    print(multiply(num, k))