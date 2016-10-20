a = 20  # global var


def add20(x):
    """
    :param x:
    :return x + 20:

    this is called doc string - like java doc

    """
    a = 10
    print(a)  # local var
    return x + a


print(add20(a))
help(add20)
