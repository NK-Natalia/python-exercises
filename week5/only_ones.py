# Dan list. Print those elements that appear
# in the list only once. Elements must be displayed
# in the order in which they appear in the list.

A = list(map(int, input().split()))

x = 0
B = []
for i in range(len(A) - 1, -1, -1):
    x = A[- 1]
    A.pop()
    B.append(x)
    for j in range(len(A)):
        if x == A[j]:
            B.pop()
            break
    A.insert(0, x)


B.reverse()
print(*B)
