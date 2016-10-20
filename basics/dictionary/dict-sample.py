# {} differentiate dictionaries from lists an tuples
# syntax is similar to JSON
# only difference between JSON and DICT is that order does not matter in DICT

dictRy = {1: "one", 2: "three", 4: "two", "er": 45}
print(type(dictRy))
print(len(dictRy))

print(dictRy[2])
dictRy[6] = "some new val"
print(dictRy)
dictRy["text"] = "some new val"  # this won't work if original declaration of DICT did not have string key

# for x in dictRy:
#     print(x, ":", dictRy[x])

dic2 = {"2": dictRy, "3": [2, 3], 3: (3, 7, 12)}
for x in dic2:
    print(x, ":", dic2[x])
