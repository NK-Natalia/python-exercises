numb = int(input())
n = 0
k = 0
while numb != 0:
    p = str('')
    k = numb
    while k != 0:
        p = p + str(k % 10)
        k = k // 10
    if p == str(numb):
        n += 1
    numb -= 1
print(n)
