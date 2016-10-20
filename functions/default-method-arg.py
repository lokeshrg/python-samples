# default arguments function
def areaofcircle(r, pi=3.14):
    return pi*r**2


print(areaofcircle(10))


def wish(name, age):
    print("hello {} your age is {}".format(name, age))


wish("John", 76)
wish(age=98, name="Unknown")  # keyword arguments
