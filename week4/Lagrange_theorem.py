# Lagrange theorem realized through recursion
import math
n = int(input())
A = list()
i = 1
N = n


def Lagrange(n):
    global A
    global i
    if n != 0:
        if len(A) < 4:
            a = math.floor(n ** 0.5)
            A.append(a)
            n = n - a ** 2
            Lagrange(n)
        elif len(A) == 4:
            n = N
            A.clear()
            a = math.floor(n ** 0.5) - 1 * i
            A.append(a)
            n = n - a ** 2
            i += 1
            Lagrange(n)


Lagrange(n)

print(*A)
