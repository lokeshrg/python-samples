import sys, math

if len(sys.argv) is 2:
    args = int(sys.argv[1])
elif len(sys.argv) < 2:
    args = int(input('Enter a number to see the number of digits in its factorial:'))
else:
    print('invalid input.. program will exit now!')

print(len(str(math.factorial(args))))
