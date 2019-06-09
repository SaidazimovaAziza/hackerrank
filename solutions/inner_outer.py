import numpy


def inner_numpy(A, B):
    return numpy.inner(A, B)


def outer_numpy(A, B):
    return numpy.outer(A, B)


A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(inner_numpy(A, B))
print(outer_numpy(A, B))