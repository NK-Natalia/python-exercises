with open('input.txt', encoding='utf8') as inFile:
    myFile = inFile.readlines()
    n = int(myFile[0])
    A = set()
    for a in range(1, n + 1):
        A.add(a)
    Nlines = len(myFile)
    YESset = set()
    YESset |= A
    NOset = set()
    for i in range(Nlines):
        set_i = set(myFile[i])
        if 'S' in set_i:
            YESlist = myFile[i - 1]
            YESadd = set()
            for new in list(map(int, YESlist.split())):
                YESadd.add(new)
            YESset &= YESadd
        elif 'N' in set_i:
            NOlist = myFile[i - 1]
            NOadd = set()
            for new in list(map(int, NOlist.split())):
                NOadd.add(new)
            NOset |= NOadd
    print(*sorted(list(YESset - NOset)))
