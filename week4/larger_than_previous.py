# The sequence consists of natural numbers and ends
# with the number 0. Determine how many elements of
# this sequence are larger than the previous element.
n = int(input())
i = 0
while n != 0:
    a = n
    n = int(input())
    if n > a:
        i += 1

print(i)
