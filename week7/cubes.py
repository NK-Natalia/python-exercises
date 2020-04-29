with open('input.txt') as myFile:
    firstLine = myFile.readline()
    a = int(firstLine.split()[0])
    X = []
    for line in myFile:
        x = int(line)
        X.append(x)
    A = X[:a]
    B = X[a:]
    setA = set(A)
    setB = set(B)
    setC = setA & setB
    C = list(setC)
    print(len(C))
    print(*sorted(C))
    Ann = setA - setC
    print(len(Ann))
    print(*sorted(Ann))
    Boris = setB - setC
    print(len(Boris))
    print(*sorted(Boris))
