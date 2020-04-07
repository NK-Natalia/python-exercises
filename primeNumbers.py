# determine if a number is prime
import math


def MinDivisor(n):
    x1 = 1
    while x1 <= math.sqrt(n):
        x1 += 1
        if n % x1 == 0:
            return x1
    return n


def isPrime(n):
    return MinDivisor(n) == n


n = int(input())

if isPrime(n):
    print('YES')
else:
    print('NO')
