with open('input.txt') as inFile:
    lines = inFile.readlines()
    myDict = {}
    i = 0
    while i < (len(lines)):
        myList = list(lines[i])
        for c in range(len(myList)):
            if myList[c] == '-':
                myList[c] = ''
            elif myList[c] == '(':
                myList[c] = ''
            elif myList[c] == ')':
                myList[c] = ''
            elif myList[c] == '+':
                myList[c] = ''
                myList[c + 1] = '8'
        myLine = ''.join(myList)
        myLine = myLine.strip()
        if len(myLine) == 7:
            myLine = '8495' + myLine
        myDict[i] = [myLine]
        i += 1
    for n in range(1, i):
        if myDict[0] == myDict[n]:
            print('YES')
        else:
            print('NO')
