# Given two integers A and B (with A≤B).
# Print all numbers from A to B inclusive.

A = int(input())
B = int(input())
A <= B


for i in range(A, B + 1):
    print(i, end=' ')
