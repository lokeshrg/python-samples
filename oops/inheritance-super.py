import simpleclass


class Life(simpleclass.Maximus):
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