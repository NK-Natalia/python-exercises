from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, m=list()):
        self.m = copy.deepcopy(m)

    def __str__(self):
        str_m = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])
        return str_m

    def size(self):
        return (len(self.m), len(self.m[0]))

    def __add__(self, other):
        res = Matrix
        res.m = []
        if len(self.m) == len(other.m):
            for i in range(len(self.m)):
                temp = []
                if len(self.m[0]) == len(other.m[0]):
                    for j in range(len(self.m[0])):
                        x = self.m[i][j] + other.m[i][j]
                        temp.append(x)
                    res.m.append(temp)
                else:
                    raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)
        return Matrix(res.m)

    def __mul__(self, alpha=0):
        c = copy.deepcopy(self.m)
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                c[i][j] = self.m[i][j] * alpha
        return Matrix(c)

    __rmul__ = __mul__

    def transpose(self):
        tmatrix = list(zip(*self.m))
        self.m = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.m))
        return Matrix(tmatrix)

exec(stdin.read())
