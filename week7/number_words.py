# The number of words in the text

with open('input.txt') as myFile:
    A = set()
    for line in myFile:
        text = list(line.split())
        for i in range(len(text)):
            A.add(text[i])
    print(len(A))
