# Given a list of numbers, which can contain up to
# 100,000 numbers. Determine how many different
# numbers there are in it.

myList = list(map(int, input().split()))
print(len(set(myList)))
