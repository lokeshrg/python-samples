from math import fabs, pi  # import specific functions rather than whole library

# from math import * is same as import math
lv1 = 34
lv3 = 'temp local variable'


def test1():
    lv4 = [1, 3]
    print(locals())
    print(globals())


test1()

print(fabs(-12.345))
print(pi)

print(__name__)
