# Move the list items to the right cyclically
# (A [0] goes to the place A [1], A [1] goes to the place
# A [2], ..., the last element goes to the place A [0]).

A = list(map(int, input().split()))

x = A[-1]
A.pop()
A.insert(0, x)

print(*A)
