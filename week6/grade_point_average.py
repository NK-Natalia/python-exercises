import statistics as st
inFile = open('./input.txt', 'r', encoding='utf8')
list9 = []
list10 = []
list11 = []
for line in inFile:
    if int(line.split()[2]) == 9:
        list9.append(int(line.split()[3]))
    elif int(line.split()[2]) == 10:
        list10.append(int(line.split()[3]))
    elif int(line.split()[2]) == 11:
        list11.append(int(line.split()[3]))

print(st.mean(list9), st.mean(list10), st.mean(list11), end=' ')
inFile.close()
