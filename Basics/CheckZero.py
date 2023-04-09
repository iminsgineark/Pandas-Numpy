import numpy
def NonZero(arr):
    for i in arr:
        if i == 0:
            return False
    return  True


arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(NonZero(arr))


mat = numpy.zeros((4,4), dtype=int)
mat[::2, 1::2] = 1
mat[1::2, ::2] = 1
print(mat)

