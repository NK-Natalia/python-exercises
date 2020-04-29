inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
A_9 = []
A_10 = []
A_11 = []
for line in inFile:
    a = int((line.split())[3])
    b = int((line.split())[2])
    if b == 9:
        A_9.append(a)
    elif b == 10:
        A_10.append(a)
    elif b == 11:
        A_11.append(a)
B = [0] * 3
a9 = max(A_9)
for now in A_9:
    if now == a9:
        B[0] += 1
a10 = max(A_10)
for now in A_10:
    if now == a10:
        B[1] += 1
a11 = max(A_11)
for now in A_11:
    if now == a11:
        B[2] += 1

print(*B, file=outFile)

inFile.close()
outFile.close()
