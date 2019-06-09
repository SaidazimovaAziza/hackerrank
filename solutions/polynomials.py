import numpy


def polynomials():
    A = [i for i in map(float, input().split())]
    b = int(input())
    return numpy.polyval(A, b)

print(polynomials())