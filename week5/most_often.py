# Without changing it or using additional lists,
# determine what number is most often found on this list.

A = list(map(int, input().split()))

x = 0
cMax = 0
ans = 0

for i in range(len(A)):
    x = A[i]
    if cMax < A.count(x):
        cMax = A.count(x)
        ans = x

print(ans)
