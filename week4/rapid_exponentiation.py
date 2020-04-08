# rapid exponentiation


def exponent(a, n):
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    return a * (a ** (n - 1))


a = float(input())
n = int(input())

print(exponent(a, n))
