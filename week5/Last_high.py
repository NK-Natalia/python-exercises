# Find the largest value in the list and
# the index of the last element that has
# the given value in one pass through the list
# without modifying this list or using an additional list.
# Print two values.

s = list(map(int, input().split()))
maxN = s[0]
idxM = 0

for i in range(1, len(s)):
    if int(s[i]) >= maxN:
        maxN = s[i]
        idxM = i

print(maxN, idxM)
