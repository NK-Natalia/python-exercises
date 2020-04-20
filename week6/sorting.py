N = int(input())
A = list(map(int, input().split()))
len(A) == N

A.sort()
print(*A)
