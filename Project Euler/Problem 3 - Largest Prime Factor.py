#!/bin/python3
import sys

def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    pdiv = []
    if isprime(n):
        return n
    for i in range(2, n + 1):
        if n % i == 0:
            pdiv.append(i)
        while (n % i == 0):
            n = n // i
            if isprime(n):
                return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime(n))

#Difficulty - Execution time. Numbers lie between 10 and 10^12
#Some test cases have prime number of size ~ 10^10 - Thus long division method fails
#Checking prime number has complexity = O(root(n))
#Long division has complexity O(n)