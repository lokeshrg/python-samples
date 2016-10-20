# function syntax - def
def add(x, y):
    assert isinstance(y, int)
    return x * y


a = add(4, 5)
print(a)


def difference(x, y):
    if x < y:
        # swap two variables
        x, y = y, x
    return x - y
