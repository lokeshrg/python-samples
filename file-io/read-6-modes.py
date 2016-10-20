# f = open('../basics/test1.py')  # by default, read[R] mode is used
# print(f.readlines())            # read all lines into a list
# f.close()
# f = open('../basics/test1.py')  # by default, read[R] mode is used
# print(f.read())                 # read whole file - at once
# f.close()
f = open('../basics/test1.py')  # by default, read[R] mode is used
print('spec char:', f.read(4))                # read char by char
f.close()
f = open('../basics/test1.py')  # by default, read[R] mode is used
print('second last line:', f.readline(-2))           # read line by line
f.close()
# f = open('../basics/test1.py', 'a')
# f.write('\n# working')
# # f.close()                     # this is necessary if opened in w mode rather than a mode
# f = open('../basics/test1.py')  # by default, read[R] mode is used
# print(f.readlines())
# f.close()
