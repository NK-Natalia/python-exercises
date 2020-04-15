# A list of numbers is given. Determine how many elements
# in this list are more than two of their neighbors
# and print the number of such elements.

s = list(map(int, input().split()))


def Same(s):
    A = list()
    for i in range(1, (len(s) - 1)):
        x1 = int(s[i - 1])
        x2 = int(s[i])
        x3 = int(s[i + 1])
        if x1 < x2 and x3 < x2:
            A.append(x2)
    print(len(A))

Same(s)
