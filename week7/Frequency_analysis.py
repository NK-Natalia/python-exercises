# Print all the words that appear in the text, one for each
# line. Words should be sorted in descending order of the
# number of occurrences in the text.

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
print('\n'.join(sorted_dict))
