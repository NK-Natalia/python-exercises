# Find the number of positive elements in a list.

numList = list(map(int, input().split()))
ans = 0

for i in numList:
    if i > 0:
        ans += 1

print(ans)
