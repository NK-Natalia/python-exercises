queen = []
hit = False
for i in range(0, 8):
    queen.append(list(map(int, input().split())))
for i in range(0, 7):
    x1 = queen[i][0]
    y1 = queen[i][1]
    for j in range(i + 1, 8):
        x2 = queen[j][0]
        y2 = queen[j][1]
        if x1 == x2 or y1 == y2 or abs(y2 - y1) == abs(x2 - x1):
            hit = True
if hit:
    print('YES')
else:
    print('NO')
