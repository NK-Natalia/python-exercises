# Print the word that is most often found in the text.
with open('input.txt') as inFile:
    myFile = inFile.readlines()
    myDict = {}
    ans = {}
    ans1 = []
    for line in myFile:
        myLine = line.split()
        for word in myLine:
            myDict[word] = myDict.get(word, 0) + 1
sorted_dict = sorted(myDict, key=lambda x: (-myDict[x], x))
print(sorted_dict[0])
