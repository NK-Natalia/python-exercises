# Rearrange the elements of this list in the reverse order,
# then display the elements of the resulting list.

A = list(map(int, input().split()))
i = 0
x = 0

while i < (len(A) // 2):
    x = A[i]
    A[i] = A[-(1 + i)]
    A[-(1 + i)] = x
    i += 1

print(*A)
