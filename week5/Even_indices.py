# Print all list items with even indices

numList = list(map(int, input().split()))
myList = numList[::2]
print(*myList)
