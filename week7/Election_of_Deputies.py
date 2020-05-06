names = list()
votes = list()
sumVotes = 0
inFile = open('input.txt')
for line in inFile:
    if len(line) < 2:
        continue
    else:
        line = line.split()
        partyName = ' '.join(line[:-1])
        partyVotes = int(line[-1])
        names.append(partyName)
        votes.append(partyVotes)
        sumVotes += partyVotes
inFile.close()

mandates = list()
fracPart = []
sumMandates = 0
for i in range(len(names)):
    partyMandates = (votes[i] * 450) / sumVotes
    sumMandates += int(partyMandates)
    mandates.append(int(partyMandates))
    fracPart.append(partyMandates - int(partyMandates))

# fracPart = enumerate(fracPart)
# , key=lambda x: (x[1], x[0]), reverse=True)
# print(mandates)
while sumMandates < 450:
    i = 0
    for j in range(1, len(fracPart)):
        if (
            (fracPart[j] > fracPart[i]) or  # если следующий остаток больше
            (fracPart[j] == fracPart[i] and votes[j] > votes[i])
                ):  # если пред и след остатки равны, но след голосов больше
            i = j
    mandates[i] += 1
    sumMandates += 1
    fracPart[i] = 0

for k in range(len(names)):
    print(names[k], mandates[k])


for k in range(len(names)):
    print(names[k], mandates[k])
