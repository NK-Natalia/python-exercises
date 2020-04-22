# The program that, given the information about users
# and free space on the archive disk, will determine the
# maximum number of users whose data can be archived.

A = list(map(int, input().split()))

S = A[0]
S <= 10000
N = A[1]
N <= 100
n = 0
n <= 1000
i = 0
I = []
for i in range(N):
    n = int(input())
    I.append(n)


I.sort()

sumI = 0
k = 0
for k in range(N):
    if sumI < S:
        sumI += I[k]
        k += 1
    else:
        break

if sumI < S:
    print(len(I))
elif sumI > S:
    print(k - 1)
elif sumI == S:
    print(k)
