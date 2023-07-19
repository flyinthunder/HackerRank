#!/bin/python3

import sys

def generate_primes(n):
    primes = [2]
    for i in range(2, n + 1):
        isprime = True
        for j in primes:
            if i % j == 0:
                isprime = False
        if isprime:
            primes.append(i)
    return primes

def smallest_multiple(n):
    if n == 1:
        return 1
    primes = generate_primes(n)
    power_of_primes = []
    for i in primes:
        j = i
        while j * i <= n:
            j = j * i
        power_of_primes.append(j)
    smallest_multiple = 1
    for i in power_of_primes:
        smallest_multiple = smallest_multiple * i
    return smallest_multiple

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))

# Multiply all powers of prime numbers.
# 1<= N <= 40 -> Time is not an issue