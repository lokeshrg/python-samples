fin = open('test.py')
print(fin.read())
# now file has reached end - so to read again open file again

offset = 20
seek_from = 0  # possible vales are 0, 1, 2
# 2 - end of file
# 1 - current location
# 0 - from beginning of file
fin.seek(offset, seek_from)
# print(fin.read())

seek_from = 1
offset = 10
fin.seek(offset, seek_from)
print(fin.readline())

# seek_from = 2
# offset = -3
# fin.seek(offset, seek_from)
# print(fin.readline())
