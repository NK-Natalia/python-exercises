# determine a place in the ranks

A = list(map(int, input().split()))
N = int(input())

s = 0
A.append(N)
i = len(A) - 1
while i != 0:
    if A[i] > A[i - 1]:
        s = A[i - 1]
        A[i - 1] = A[i]
        A[i] = s
    else:
        break
    i -= 1

print(i + 1)
