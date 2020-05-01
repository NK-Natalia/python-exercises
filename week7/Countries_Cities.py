with open('input.txt', encoding='utf8') as inFile:
    myDict = {}
    for line in inFile:
        line = line.strip()
        myList = list(line.split())
        if len(myList) > 1:
            for i in range(1, len(myList)):
                myDict[myList[i]] = myList[0]
        elif len(myList) == 1:
            if line.isdigit():
                continue
            else:
                print(myDict[line])
