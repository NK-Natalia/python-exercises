# counting the sum of numbers in a sequence
# of numbers using recursion


def sumseq():
    n = int(input())
    if n != 0:
        return n + sumseq()
    return 0


print(sumseq())
