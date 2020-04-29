n = int(input())
N = list(map(int, input().split()))
k = int(input())
K = list(map(int, input().split()))

X = [0] * n
for i in range(k):
    a = K[i]
    X[a - 1] += 1
for nowX in range(n):
    if X[nowX] > N[nowX]:
        print('YES')
    else:
        print('NO')
