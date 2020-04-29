# The input line contains a sequence of numbers separated by spaces.
# For each number print the word YES (in a separate line) if this number
# was previously encountered in the sequence or NO if it did not.
A = list(map(int, input().split()))
B = set()
b = len(B)
for i in range(len(A)):
    B.add(A[i])
    if len(B) > b:
        print('NO')
        b = len(B)
    else:
        print('YES')
