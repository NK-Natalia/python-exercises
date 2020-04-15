# The numbers a, b, c, d, e are given.
# Count the number of integers from 0
# to 1000 (inclusive) that are the roots of
# the equation (ax³ + bx² + cx + d) / (x-e) = 0,
# and print their number.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
i = 0

for x in range(1001):
    if x != e:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            i += 1


print(i)
