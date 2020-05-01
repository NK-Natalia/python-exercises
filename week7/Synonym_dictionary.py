# given a dictionary consisting of pairs of words.
# Each word is synonymous with a pair of words.
# All words in the dictionary are different.
# For one given word, define its synonym

with open('input.txt') as inFile:
    Syn_dict = {}
    lines = inFile.readlines()
    for line in lines:
        myLine = list(line.split())
        if len(myLine) > 1:
            Syn_dict[myLine[0]] = myLine[1]
            Syn_dict[myLine[1]] = myLine[0]
    print(Syn_dict[(lines[-1].strip())])
