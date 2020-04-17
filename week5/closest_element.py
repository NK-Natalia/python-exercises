# The program that finds the element closest
# in magnitude to a given number in the array.

N = int(input())
A = list(map(int, input().split()))
x = int(input())
B = []
y = 0

for i in range(N):
    B.append(abs(A[i] - x))

a = min(B)
i = B.index(a)

print(A[i])
