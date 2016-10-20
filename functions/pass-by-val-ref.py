# passing list by reference
def pb_ref(x):
    x.pop()


a = [3, 4, 7, 1, 10]
pb_ref(a[:])  # pass by value - this is because we are not passing by value, we are sending reference
print(a)
pb_ref(a)
print(a)


# dict pass by value
def pb_val(x, key):
    x.pop(key)


b = {1: "xyz", 2: "and"}
print(b)
pb_ref(b)
pb_val(b, 2)
print(b)


