#!/bin/python3

import sys

def generate_primes(n=999999, r_type="dict"):
    primes = [True for i in range(n)]
    current = 2
    while current * current <= len(primes):
        if primes[current]:
            for i in range(current * current, n, current):
                primes[i] = False
        current += 1
    if r_type == "raw":
        return primes

    count = 0
    sum = 0
    primes_dict = {}
    for i in range(2, len(primes)):
        if primes[i]:
            sum += i
            primes_dict[i] = sum
            count += 1
    if r_type == "dict":
        return primes_dict

def sum_primes(n, primes):
    for i in range(n, 0, -1):
        if i in primes.keys():
            return primes[i]
        else:
            pass

t = int(input().strip())
primes = generate_primes(1000000, "dict")
for a0 in range(t):
    n = int(input().strip())
    print(sum_primes(n, primes))