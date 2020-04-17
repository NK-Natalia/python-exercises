# In the list, all elements are pairwise different.
# Swap the minimum and maximum element of this list.

A = list(map(int, input().split()))

imax = A.index(max(A))
imin = A.index(min(A))
A[imin], A[imax] = A[imax], A[imin]

print(*A)
