with open('input.txt', 'r', encoding='utf8') as inFile:
    nameDict = {}
    for line in inFile:
        name = line.strip()
        nameDict[name] = nameDict.get(name, 0) + 1
    countDict = {}
    for name in nameDict:
        count = (nameDict[name])
        countDict[count] = name
    countList = []
    for count in countDict:
        countList.append(count)
    sumCount = sum(countList)
    a = max(countList)
with open('output.txt', 'w', encoding='utf8') as outFile:
    if a > sumCount / 2:
        print(countDict[a], file=outFile)
    else:
        print(countDict[a], file=outFile)
        countList.remove(a)
        a = max(countList)
        print(countDict[a], file=outFile)
