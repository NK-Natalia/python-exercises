# For a given positive integer n, calculate
# the sum 1! +2! +3! + ... + n !.

n = int(input())
x = 1
ans = 0

for i in range(1, n + 1):
    x *= i
    ans += x
print(ans)
