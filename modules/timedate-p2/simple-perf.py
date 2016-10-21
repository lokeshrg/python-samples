import time, datetime

starttime = datetime.time().microsecond

for x in range(1000):
    print(x ** x)  # compute the power of numbers from 1 to 1000

endtime = datetime.datetime.now().microsecond #icrosecond

print(endtime - starttime)
