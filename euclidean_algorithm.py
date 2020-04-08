# Euclidean algorithm implemented through recursion


def gcd(a, b):
    if b % a != 0:
        return gcd(b % a, a % (b % a))
    return a


a = int(input())
b = int(input())

print(gcd(a, b))
