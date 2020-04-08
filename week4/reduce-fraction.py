# reduce fraction implemented through recursion


def gcd(m, n):
    if n % m != 0:
        return gcd(n % m, m % (n % m))
    return m


def ReduceFraction(m, n):
    p = m / gcd(m, n)
    q = n / gcd(m, n)
    return int(p), int(q)


m = int(input())
n = int(input())

print(*ReduceFraction(m, n))
