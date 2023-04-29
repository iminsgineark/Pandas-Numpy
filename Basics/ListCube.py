def cube(x):
    return x * x * x


List = [1, 2, 3, 4, 5, 6, 7, 8]
# newl = []
# for i in List:
#     newl.append(cube(i))
newl = list(map(cube, List))
print(newl)

#
# def Filter_Func(X):
#     if X % 2 != 0:
#         return X
newl1 = list(filter(lambda X: X % 2 != 0, List))
print(newl1)

from functools import reduce
import math


def Lcm():
    return math.lcm()


newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList1 = [5, 20]
# Sum = reduce(lambda X,Y:X%Y,newList)
GreatestNum = reduce(lambda X, Y: X if X > Y else Y, newList)
SmallestNum = reduce(lambda a, b: a if a < b else b, newList)
LCM = (lambda X: Lcm, newList1)

print(LCM)
