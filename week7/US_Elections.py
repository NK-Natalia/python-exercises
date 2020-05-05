with open('input.txt', 'r', encoding='utf8') as inFile:
    nameDict = {}
    for line in inFile:
        name = list(line.split())[0]
        vote = list(line.split())[-1]
        nameDict[name] = nameDict.get(name, 0) + int(vote)
    for name in sorted(nameDict):
        print(name, nameDict[name])
