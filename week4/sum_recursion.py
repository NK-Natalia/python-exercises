# calculate the sum of two numbers with recursion


def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)


a = int(input())
b = int(input())
a <= 900
b <= 900

print(sum(a, b))
