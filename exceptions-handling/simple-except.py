# handling exceptions
for x in range(3):
    try:
        amount = int(input('Enter the amount:'))
        break
    except ValueError:
        print('Enter a valid number, you have {} more tries'.format(2-x))
else:  # this else is for 'FOR' in python
    print('Exiting')