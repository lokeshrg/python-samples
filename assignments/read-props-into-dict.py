sf = open('../settings.txt', 'r')

settingsDict = {}
for word in sf:
    if word.startswith('#') or "=" not in word:  # word.__contains__("="):
        continue
    key, value = word.strip().split('=')   # single line, auto assign two items to two var
    # settingsDict.__setitem__(word[0], word[1])
    settingsDict[key] = value

print(settingsDict.items())
