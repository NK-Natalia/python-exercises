# Print the value of the smallest odd list item.

s = list(map(int, input().split()))
A = list()
for i in range(len(s)):
    if int(s[i]) % 2 != 0:
        A.append(int(s[i]))

minA = int(A[0])
for a in range(len(A)):
    if A[a] < minA:
        minA = A[a]

print(minA)
