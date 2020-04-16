# Given a list of numbers and the index of the
# element in the list k. Remove the element with
# index k from the list by moving to the left all
# the elements to the right of the element with index k.

a = list(map(int, input().split()))
k = int(input())

x = a[k]
for i in range(k, (len(a) - 1)):
    a[i] = a[i + 1]

a[-1] = x
a.pop()
print(*a)
