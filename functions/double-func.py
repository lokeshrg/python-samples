# we can define and consume two vars
def sumdiff(x, y):
    return x + y, x - y


mysum, mydiff = sumdiff(40, 23)
print("sum: ", mysum, "diff: ", mydiff)
