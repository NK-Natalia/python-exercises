# A list of integers is given. It is required to “squeeze”
# it by moving all nonzero elements to the left side of the list,
# without changing their order, and all zeros to the right side.

A = list(map(int, input().split()))

i = 0
y = 0
while i < len(A) - y:
    if A[i] == 0:
        A.pop(i)
        A.append(0)
        y += 1
    else:
        i += 1

print(*A)
