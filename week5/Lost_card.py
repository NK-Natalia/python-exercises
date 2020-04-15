# For a board game, cards with numbers from
# 1 to N are used. One card is lost. Find her,
# knowing the numbers of the remaining cards.

N = int(input())

A = 0
for i in range(1, N):
    n = int(input())
    A += n

B = N * ((N + 1) / 2)

print(int(B - A))
