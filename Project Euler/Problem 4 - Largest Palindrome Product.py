#!/bin/python3

import sys

def ispalindrome(n):
    return str(n)[0:3] == "".join(list(reversed(str(n)))[0:3])

def palindrome(n):
    for i in range(n, 1, -1):
        if ispalindrome(i):
            for j in range(100,1000):
                if i%j==0:
                    if len(str(i//j))==3:
                        return i      

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(palindrome(n-1))

#Find number less then n that is a palindrome made by multiplying 2 three digit numbers.
#For this first iterate over numbers from n to 0.
# For each number i, check if i is a palindrome.
# If i is a palindrome, check if it is divisible by a 3 digit number.
# if it is, divide i by the number and check if the answer is also 3 digits.