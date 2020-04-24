# Given a list of N (N≤2 * 10⁵) elements that
# take integer values from 0 to 100 (100 including).
# Sort this list in non-decreasing order. Print the resulting list.

numbers = list(map(int, input().split()))
newNumbers = [0] * 101
for number in numbers:
    newNumbers[number] += 1
for nowNumber in range(101):
    print((str(nowNumber) + ' ') * newNumbers[nowNumber], end='')
