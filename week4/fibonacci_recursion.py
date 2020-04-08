# returns the number of fibonacci by its position number using recursion


def phib(n):
    if n <= 1:
        return n
    else:
        return phib(n - 1) + phib(n - 2)


n = int(input())

print(phib(n))
