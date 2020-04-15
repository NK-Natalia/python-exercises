# A list of numbers is given. Print the value of
# the largest element in the list, and then the index
# of this element in the list. If there are several largest elements,
# print their value and the index of the first of them.

s = list(map(int, input().split()))
maxN = int(s[-1])
idxM = int(len(s)) - 1

for i in range(len(s) - 1, 0, -1):
    if int(s[i]) >= maxN:
        maxN = s[i]
        idxM = i
if int(s[0]) >= maxN:
        maxN = s[0]
        idxM = 0

print(maxN, idxM)
