
def fibonac(max):
    x, y = 0, 1
    while x < max:
        print(x)
        x, y = y, x + y


fibonac(1000)
