with open('input.txt', 'r', encoding='utf8') as inFile:
    newList = []
    lines = inFile.readlines()
    for line in lines:
        if len(line.split()) == 1:
            N = int(line.split()[0])
        elif len(line.split()) > 1:
            r_1 = (line.split())[-1]
            r_2 = (line.split())[-2]
            r_3 = (line.split())[-3]
            if int(r_1) > 39 and int(r_2) > 39 and int(r_3) > 39:
                newList.append(int(r_1) + int(r_2) + int(r_3))
with open('output.txt', 'w', encoding='utf8') as outFile:
    if len(newList) <= N:
        print(0, file=outFile)
    elif N == 0:
        print(0, file=outFile)
    else:
        newList.sort()
        newList.reverse()
        k = N - 1
        if newList[k] > newList[k + 1]:
            print(newList[k], file=outFile)
        elif newList[k] == newList[0]:
            print(1, file=outFile)
        else:
            A = []
            A.extend(newList[0:k])
            A.sort()
            for a in A:
                if a > newList[k]:
                    print(a, file=outFile)
                    break
