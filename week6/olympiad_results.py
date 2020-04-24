# Arrange the list of participants in the Olympiad
# in descending order of scores.
with open('input.txt', 'r', encoding='utf8') as inFile:
    for lines in inFile:
        lines = inFile.readlines()
        newList = []
        for line in lines:
            name = (line.split())[0]
            result = (line.split())[1]
            newList.append((int(result), name))
        newList.sort()
        newList.reverse()
        for new in newList:
            print(new[1])
