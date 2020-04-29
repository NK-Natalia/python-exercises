inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
A = [0] * 12
for line in inFile:
    a = int((line.split())[3])
    b = int((line.split())[2])
    if a > A[b]:
        A[b] = a
print(*A[9:12], file=outFile)

inFile.close()
outFile.close()
