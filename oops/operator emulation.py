# operator emulation
# __operator__ : if you add this method in class - it defines how it works
# eg. __sub__ defines how obj1 - ob2 works
# eg. __add__ defines how obj1 + ob2 works

class Car:
    def __init__(self, seats):
        self.seats = seats

    def __add__(self, other):  # this is over riding the bevaior of symbol + i.e., add
        return self.seats + other.seats

    def __sub__(self, other):
        return 'subtraction over ridden!'

zen = Car(4)
swift = Car(5)

print(zen + swift)
print(zen - swift)
