fin = open("read-6-modes.py")
# print(help(dir(fin)))
print(fin.name)
print(fin.buffer)
print(fin.mode)
print(fin.closed)
print(fin.errors)

for line in fin:
    print(line, end='', sep='123')

fin.close()
print(fin.closed)
