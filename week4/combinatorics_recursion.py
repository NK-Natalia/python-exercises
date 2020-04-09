# counting the number of combinations of k elements
# in the sequence of n numbers


def C(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k == 0:
        return 1
    while n != 0:
        return C(n - 1, k) + C(n - 1, k - 1)


n = int(input())
k = int(input())
0 <= k <= n
print(C(n, k))
