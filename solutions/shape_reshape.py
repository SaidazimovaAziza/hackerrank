import numpy


def shape_reshape():
    my_array = numpy.array(list(map(int,input().split())))
    return numpy.reshape(my_array, (3, 3))


print(shape_reshape())
