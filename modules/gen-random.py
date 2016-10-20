import random


# def rand(min, max):
#     return random.randint(min, max)


r = []
for x in range(100):
    r.append(random.randint(70, 100))

print(len(r))
print(r.count(99))
