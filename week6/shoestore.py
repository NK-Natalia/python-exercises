# It is known that one pair of shoes can be worn
# on another if it is at least three sizes larger.
# The buyer came to the store. It is required to
# determine how many pairs of shoes the seller can
# offer him so that he can put them all on at the same time.


N = int(input())
A = list(map(int, input().split()))
B = []
C = []
for i in range(len(A)):
    if A[i] >= N:
        B.append(A[i])
B.sort()
if len(B) > 0:
    n = B[0]
    C.append(B[0])
    for b in range(len(B)):
        if B[b] - n >= 3:
            n = B[b]
            C.append(n)

print(len(C))
