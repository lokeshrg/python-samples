# import simpleclass
# OR
from simpleclass import Maximus


# class Life(simpleclass.Maximus):
class Life(Maximus):
    def __init__(self):
        self.exam = 'test'
        self.superv = '1'
    def testIn(self):
        self.superv = super(Life, self).name

test = Life()
print(test.exam)
print(test.superv)
test.testIn()
print(test.superv)