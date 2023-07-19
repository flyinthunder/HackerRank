#!/bin/python3

import sys

def multi(n):
    largest3 = (n-1)//3
    largest5 = (n-1)//5
    largest15 = (n-1)//15

    component3 = (largest3*(largest3+1)//2)*3
    component5 = (largest5*(largest5+1)//2)*5
    component15 = (largest15*(largest15+1)//2)*15
    total = component3 + component5 - component15
    return total

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(multi(n))

#Difficulty - Execution time. Numbers lie between 10 and 10^9
#Counting each number or using sum(range(n)) is not ideal.
#Sum of all digits (1-n) is given by n(n+1)/2 - This has time complexity of O(1)
#Problem can be broken down as follows -
#We need sum of all numbers below n divisible by 3 or 5 -> This can be obtained by getting sum of largest multiple ->
# For = 10, largest multiple of 3 is 9 = 3*3
# Thus contribution made by multiples of 3 = (1+2+3)*3
# Similar calculation for 5
# As multiples of 15 are accounted twice, we subtract them once.