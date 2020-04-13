# Given a natural number n. Print all n-digit
# odd positive integers in descending order.

n = int(input())

for i in range((10 ** n) - 1, (10 ** (n - 1) - 1), -2):
    print(i, end=' ')
