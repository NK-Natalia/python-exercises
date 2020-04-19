def intersection(a, b):
    c = []
    x = y = 0
    while x < len(a) and y < len(b):
        if b[y] < a[x]:
            y += 1
        elif b[y] == a[x]:
            c.append(b[y])
            y += 1
            x += 1
        elif b[y] > a[x]:
            x += 1
    return c


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*intersection(A, B))
