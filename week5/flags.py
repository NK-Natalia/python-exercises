# the program draws flags.
# Their number is equal to n.
# Each flag contains its number.

n = int(input())
1 <= n <= 9

print(('+___' + ' ') * n)
for i in range(1, n + 1):
    print('|', i, ' ', '/', sep='', end=' ')
print()
print(('|__\\' + ' ') * n)
print(('|   ' + ' ') * n)
