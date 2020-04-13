# Given two integers A and B.
# Print all numbers from A to B inclusive,
# in ascending order if A <B,
# or in decreasing order otherwise.

A = int(input())
B = int(input())


if A < B:
    for i in range(A, B + 1):
        print(i, end=' ')

if A >= B:
    for i in range(A, B - 1, -1):
        print(i, end=' ')
