# A list of numbers is given. Count how many
# pairs of elements there are equal to each other.
# It is believed that any two elements equal to
# each other form one pair, which must be calculated.

A = list(map(int, input().split()))

B = ()
x = 0
k = 0

for i in range(len(A) - 1, -1, -1):
    x = A[i]
    A.pop(i)
    for j in range(len(A)):
        if x == A[j]:
            k += 1


print(k)
