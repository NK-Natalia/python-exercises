A = list(map(int, input().split()))
B = list(map(int, input().split()))


def merge(a, b):
    x = y = 0
    c = []
    while x < len(a) and y < len(b):
        if a[x] > b[y]:
            c.append(b[y])
            y += 1
        else:
            c.append(a[x])
            x += 1
    for i in range(x, len(a)):
        c.append(a[i])
    for i in range(y, len(b)):
        c.append(b[i])
    return c


print(*merge(A, B))
