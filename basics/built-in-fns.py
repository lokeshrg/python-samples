marks = [12, 34, 32, 64, 54, 98]
# print(sum(marks))
# print(len(marks))
# print(min(marks))
# print(max(marks))
#
# print(marks[2:])
# marks[3] = 11123
print(marks)
# print(marks[:-1])

marks.append(54)

marks.insert(3, 12)
marks.append(149)
print(marks)
marks.pop()
print(marks)
marks.pop(3)  # remove by index
print(marks)

marks.remove(54)  # only removes first occurrence
print(marks)

marks.sort()
print(marks)
# marks.__format__()
marks.reverse()
print(marks)
# print(marks)
