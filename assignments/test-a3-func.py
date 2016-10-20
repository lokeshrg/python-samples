# take int and return factorial
def factorial(x):
    fact = 1
    for y in range(2, x+1):
        fact *= y
    return y
    # fact = x
    # while x != 1:
    #     fact *= x - 1
    #     x -= 1
    # return fact

ip = int(input('Enter a number to see its factorial: '))
print(ip)
print(factorial(ip))
