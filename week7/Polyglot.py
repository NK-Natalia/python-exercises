with open('input.txt', 'r', encoding='utf8') as inFile:
    head = [next(inFile) for x in range(1)]
    n = head[0]
    A = set()
    unique = set()
    NOTunique = list()
    for now in range(10):
        A.add(str(now))
    for line in inFile:
        if line[0] not in A:
            if line.split()[0] not in unique:
                unique.add(line.split()[0])
                NOTunique.append(line.split()[0])
            elif line.split()[0] in unique:
                NOTunique.append(line.split()[0])
    All = set()
    array = NOTunique
    array_d = {}.fromkeys(array, 0)
    for a in array:
        array_d[a] += 1
        if int(array_d[a]) == int(n):
            All.add(a)

    print(len(All))
    print('\n'.join(map(str, All)))
    print(len(unique))
    print('\n'.join(map(str, unique)))
