# Greatest product of three numbers

A = list(map(int, input().split()))

if len(A) == 3:
    print(*A)
else:
    Max1 = A[0]
    Min1 = A[0]

    for i in range(1, len(A)):
        if A[i] > Max1:
            Max1 = A[i]
        if A[i] < Min1:
            Min1 = A[i]

    A.remove(Max1)
    A.remove(Min1)

    Max2 = A[0]
    Min2 = A[0]

    for i in range(1, len(A)):
        if A[i] > Max2:
            Max2 = A[i]
        if A[i] < Min2:
            Min2 = A[i]

    A.remove(Max2)

    Max3 = A[0]

    for i in range(1, len(A)):
        if A[i] > Max3:
            Max3 = A[i]

    if Min1 * Min2 * Max1 > Max1 * Max2 * Max3:
        print(Min1, Min2, Max1)
    else:
        print(Max1, Max2, Max3)
