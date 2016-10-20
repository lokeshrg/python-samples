import glob

print(len(glob.glob("../../basics/*_.py")))

specials = '_'

for char in specials:
    pattern = '../*' + glob.escape(char) + '.py'
    print('Searching for: {!r}'.format(pattern))
    for name in sorted(glob.glob(pattern)):
        print(name)
    print()