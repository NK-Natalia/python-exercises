# For a given positive integer n,
# calculate the sum 1² + 2² + 3² + ... + n².

n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i * i
print(sum, end=' ')
