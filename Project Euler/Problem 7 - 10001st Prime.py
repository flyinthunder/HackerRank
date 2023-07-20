#!/bin/python3

import sys

primes = [True for i in range(9999999)]
current = 2
while current * current <= len(primes):
    if primes[current]:
        for i in range(current * current, 9999999, current):
            primes[i] = False
    current += 1

count = -2
primes_dict = {}
for i in range(len(primes)):
    if primes[i]:
        count += 1
        primes_dict[count] = i

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes_dict[n])

# Sieve method for generating primes
# Not using function so that prime number calculation only happens once.
# 1<= n <= 10^4 so can be brute forced.