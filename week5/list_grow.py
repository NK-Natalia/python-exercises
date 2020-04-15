# Determine if a list is monotonically increasing.


def IsAscending(A):
    i = 1
    maxN = A[0]
    while i < len(A) and A[i] > maxN:
        maxN = A[i]
        i += 1
    return i - len(A) == 0

A = list(map(int, input().split()))
IsAscending(A)
if IsAscending(A) is True:
    print('YES')
elif IsAscending(A) is False:
    print('NO')
