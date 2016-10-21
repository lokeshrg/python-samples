import datetime

d = datetime.datetime.now()
print(d)  # python 2.x supports print d - instead of print(d)

indian_date = str(d.day) + '/' + str(d.month) + '/' + str(d.year)
print(indian_date)