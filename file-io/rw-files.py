f = open('test.py', 'w')  # open file in write mode
f2 = open('rw-files.py', 'r')
for word in f2:
    if word.__contains__('for'):
        break
    f.write(word)
f.close()
f2.close()

words = ['res', 'test']   # use list as input to file
f = open('test.py', 'a')  # append mode
for word in words:
    f.write('\n# ' + word)
f.close()
