import os

for (dirname, subdur, files) in os.walk("C:/"):
    for file in files:
        filename = os.path.join(dirname, file)
        if filename.endswith('.jpg'):
            print(filename, os.stat(filename).st_size)