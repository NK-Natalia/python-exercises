with open('input.txt') as inFile:
    nameDict = {}
    voteList = []
    for line in inFile:
        name = str(list(line.split())[:-1])
        vote = list(line.split())[-1]
        nameDict[vote] = name
        voteList.append(int(vote))
    print(nameDict)
    print(voteList)
    firstNumber = sum(voteList) / 450
    print(firstNumber)
    voteListN = []
    voteListNfraction = []
    voteDictN = {}
    for vote in voteList:
        x1 = vote // firstNumber
        voteListN.append(x1)
        voteListNfraction.append(vote % firstNumber)
        voteDictN[x1] = nameDict[str(vote)]
    print(voteListN)
    print(voteDictN)
    print(voteListNfraction)
    controlNumber = sum(voteListN)
    if controlNumber == 450:
        print(voteDictN[x1], x1)
    print(controlNumber)
    else:
        for vote in votelist:

