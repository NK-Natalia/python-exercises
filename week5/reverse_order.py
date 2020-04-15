# Print all elements of this list in the reverse
# order, without changing the list itself.

A = list(map(int, input().split()))
B = list()

for i in range(len(A) - 1, -1, -1):
    B.append(int(A[i]))

print(*B)
