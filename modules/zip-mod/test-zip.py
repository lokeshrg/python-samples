
# from zipfile_infolist import print_info
import zipfile, glob, os

os.chdir('C:/Users/admin/Documents/python-samples/basics')
pyfiles = glob.glob('*.py')
print(pyfiles)
zipf = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
for file in pyfiles:
    zipf.write(file)

zipf.close()

