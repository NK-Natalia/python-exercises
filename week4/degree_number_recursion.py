# calculating the degree of a number
a = float(input())
a > 0
n = int(input())
n >= 0


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


print(power(a, n))
