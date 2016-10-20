csvFile = open('../resources/sample.csv')
lines = csvFile.readline()[1:]
insuranceDict = {}
for line in lines:
    # if ',' not in line:
    #     continue
    print()
    policyId, d11, d12 = line.strip().split(',')
    if float(d12) > 100000:
        print(policyId, d11, d12, sep=' : ')
