from sys import stdin
import copy


class Matrix:
    def __init__(self, m=list()):
        self.m = copy.deepcopy(m)

    def __str__(self):
        str_m = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])
        return str_m

    def size(self):
        return (len(self.m), len(self.m[0]))

exec(stdin.read())
