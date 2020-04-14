# Print all the even elements of the list.

numList = list(map(int, input().split()))
myList = list()

for i in numList:
    if i % 2 == 0:
        myList.append(i)


print(*myList)
