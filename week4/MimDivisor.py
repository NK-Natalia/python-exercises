# determine the minimum divisor of a number
import math


def MinDivisor(n):
    x1 = 1
    while x1 <= math.sqrt(n):
        x1 += 1
        if n % x1 == 0:
            return x1
    return n

n = int(input())

print(MinDivisor(n))