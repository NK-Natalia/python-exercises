# Two lists of numbers are given that can contain
# up to 10,000 numbers each. Print all the numbers
# that appear in both the first and second list,
# in ascending order.

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(list(set(a) & set(b))))
