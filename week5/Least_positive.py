# Print the value of the smallest of all
# positive elements in the list.

print(min(int(i) for i in input().split() if int(i) > 0))
