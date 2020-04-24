# Sort the list of participants alphabetically
# from and to external files

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()
lines.sort()
for line in lines:
    line = (line.split())
    line.pop(2)
    print(*line, file=outFile)
