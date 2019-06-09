import numpy


def concatenate():
    N, M, P = map(int, input().split())

    NP = numpy.array([input().split() for i in range(N)], int)
    MP = numpy.array([input().split() for j in range(M)], int)

    return numpy.concatenate((NP, MP), axis=0)


print(concatenate())

