# Given a list of integers, the number k and
# the value of C. It is necessary to insert into
# the list at the position with index k an element
# equal to C, shifting all elements with an index
# of at least k to the right.

a = list(map(int, input().split()))
k, C = map(int, input().split())

a.append(C)
for i in range((len(a) - 1), k, -1):
    x = a[i - 1]
    a[i - 1] = a[i]
    a[i] = x

print(*a)
