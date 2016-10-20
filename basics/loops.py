count = 0

'''
while count < 10:
    print(count)
    count += 1
'''

city = "Kaila same Shiva!"
print(city)
'''
for x in city:
    print(x)
'''
for index, char in enumerate(city):
    # print(index+"..."+char)#gives error
    print("index()... char()".format(index, char))
