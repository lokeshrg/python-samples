# tuples are immutable versions of lists
# syntax difference is use () instead of []
obj_tuple = (2, 3, 4, 65, 21, 12, 3)
print(obj_tuple[-2:])
print(obj_tuple.index(65))
print(type(obj_tuple))

obj_list = [13, 11, 4, 7, 18]
print(obj_list)

print(obj_tuple*2)
# print(obj_list+obj_tuple)  # won't work - incompatible types

# obj_list = obj_tuple
# obj_list.sort()  # won't work

obj_tuple = obj_list
obj_tuple.sort()
print(obj_tuple)
