# Given a few numbers. Count how many
# of them are equal to zero, and print this number.

N = int(input())
i = 1
x = 0

while i <= N:
    n = int(input())
    i += 1
    if n == 0:
        x += 1

print(x)
