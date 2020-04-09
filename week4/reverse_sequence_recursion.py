# output a sequence of numbers in reverse
# order using recursion


def rev():
    n = int(input())
    if n == 0:
        print(0)
    else:
        rev()
        print(n)


rev()
