with open('input.txt') as inFile:
    myDict = {}
    for line in inFile:
        Name = str(line.split()[0])
        product = str(line.split()[1])
        quantity = int(line.split()[2])
        if Name not in myDict:
            myDict[Name] = myDict.get(Name, {})
        myDict[Name][product] = myDict[Name].get(product, 0) + quantity
for entry in sorted(myDict):
    print(entry, ':', sep='')
    for entry2 in sorted(myDict[entry]):
        print(entry2, myDict[entry][entry2])
