# import file
import os


class MyFile:
    def __init__(self, name):
        self.name = name
        self.file = open(self.name)


    def getSize(self):
        return self.file.__sizeof__()
        # return os.stat(self.name).st_size


    def nthline(self, index):
        return self.file.readlines()[index].strip()


    def closefile(self):
        self.file.close()

# myFile2 = MyFile()
# print(myFile2.file)
myFile = MyFile('test-a2.py')
print(myFile.getSize())
print(str(myFile.nthline(3)))
print(myFile.file.closed)
myFile.closefile()
print(myFile.file.closed)