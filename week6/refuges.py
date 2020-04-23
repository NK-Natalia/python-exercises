# It is known that all n villages of the region are located along
# one straight road. There are also m shelters along the road,
# in which villagers can take refuge in the event of an attack.
# it is necessary for each village to determine the closest refuge to it.

v = int(input())
V = list(map(int, input().split()))
len(V) == v
r = int(input())
R = list(map(int, input().split()))
len(R) == r


def toTuple1(vil):
        return vil[1]


def toTuple0(ref):
    return ref[0]


A = []
for i in range(v):
    A.append((i + 1, V[i]))
A.sort(key=toTuple1)
B = []
for i in range(r):
    B.append((i + 1, R[i]))
B.sort(key=toTuple1)
Ans = []
m = 1
for n in range(v):
    a = toTuple1(A[n])
    while m <= len(B):
        if m == len(B):
            m = 0
        x = toTuple1(B[m - 1])
        y = toTuple1(B[m])
        if abs(a - x) <= abs(a - y):
            Ans.append((toTuple0(A[n]), toTuple0(B[m - 1])))
            break
        elif abs(a - x) > abs(a - y):
            m += 1
Ans.sort(key=toTuple0)

for i in range(len(Ans)):
    print(Ans[i][1], end=' ')
