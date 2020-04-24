# Arrange the list of participants in the Olympiad
# in descending order of scores.

inFile = open('input.txt', 'r', encoding='utf8')

for i in 
lines = inFile.readlines()

lines.sort()
for line in lines:
    line = (line.split())
    line.pop(2)
    print(*line, file=outFile)

