# Given two four-digit numbers A and B.
# Print all four-digit numbers on the segment
# from A to B, the record of which is a palindrome.

A = int(input())
B = int(input())
999 < A <= 9999
999 < B <= 9999

for i in range(A, B + 1):
    if (i // 100) == ((i % 10) * 10 + (i % 100 - i % 10) // 10):
        print(i)
