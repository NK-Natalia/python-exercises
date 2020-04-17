# Rearrange adjacent elements of the list
# (A [0] and A [1], A [2] and A [3], etc.).
# If there are an odd number of elements,
# the last element remains in its place.

A = list(map(int, input().split()))

c = 0
for i in range(len(A) - 1):
    if i % 2 == 0:
        c = A[i + 1]
        A[i + 1] = A[i]
        A[i] = c

print(*A)
