# A list of numbers is given. If it has two adjacent
# elements of the same sign, print these numbers.

s = list(map(int, input().split()))


def Same(s):
    for i in range((len(s) - 1)):
        x1 = int(s[i])
        x2 = int(s[i + 1])
        if x1 * x2 >= 0:
            print(x1, x2)
            break


Same(s)
