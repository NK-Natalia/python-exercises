# Given a natural number n≤9, output a ladder
# from n steps, the i-th step consists
# of numbers from 1 to i without spaces.

n = int(input())
n <= 9

for i in range(1, n + 1):
    for c in range(1, i + 1):
        print(c, end='')
    print()
