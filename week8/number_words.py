inFile = open('input.txt')
lines = str(inFile.readlines()).split()
print(*lines)
Set = set(lines)