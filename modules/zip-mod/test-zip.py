
# from zipfile_infolist import print_info
import zipfile, glob, os

os.chdir('C:/Users/admin/Documents/python-samples')
pyfiles = glob.glob('*.py')

zipf = zipfile.ZipFile('test.zip', 'w')
for file in pyfiles:
    zipf.write(file)

zipf.close()

