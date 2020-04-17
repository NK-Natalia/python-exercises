# A list ordered by non-decreasing elements in it.
# Determine how many different elements are in it.

A = list(map(int, input().split()))

s = 1
for i in range(len(A) - 1):
    if A[i + 1] != A[i]:
        s += 1

print(s)
