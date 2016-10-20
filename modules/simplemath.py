def testfn(x):
    return 34 * x


def tf2():
    return 10


def main():
    print(testfn(10) * tf2())


# print(__name__)  # this will print the origin of request of this module / script
# i.e., when run as a script[python program] __name__ = __main__
# when run as a module from another program/scipt, __name__ = <name of module> [here it is simplemath]
if __name__ == '__main__':
    # this code is specific to this program - not when it is used as a external module
    main()

if __name__ == 'simplemath':
    # this is when used as a external module
    print("Hope you like our module!")
