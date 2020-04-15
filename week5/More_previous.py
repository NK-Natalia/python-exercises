# A list of numbers is given. Print all list
# items that are larger than the previous item.

s = list(map(int, input().split()))
maxN = s[0]
ans = list()

for i in range(1, len(s)):
    if int(s[i]) > int(s[(i - 1)]):
        ans.append(s[i])


print(*ans)
