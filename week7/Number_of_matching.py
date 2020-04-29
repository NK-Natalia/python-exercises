# Two lists of numbers are given, which can contain
# up to 100,000 numbers each. Calculate how many numbers
# are contained simultaneously in both the first list and the second.

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(len(set(a) & set(b)))
