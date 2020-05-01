# For each word from the text, count how many times
# it has appeared in this text before.

with open('input.txt') as inFile:
    myFile = inFile.readlines()
    myDict = {}
    ans = list()
    for line in myFile:
        myLine = line.split()
        for word in myLine:
            myDict[word] = myDict.get(word, 0) + 1
            ans.append(myDict[word] - 1)
    print(*ans)
