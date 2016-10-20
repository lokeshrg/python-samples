
# --test--

a, b = True, False  # simultaneous assignment in order
print(a and b)
print(not a)

listTemp = [0, 0.2, 3, 'test', []]
for x in listTemp:
    if x == 'test':
        break
    elif x == 0.2:
        continue
    else:
        pass  # place holder for future action -
        # does nothing - just syntactic sugar - for empty space to make syntax correct
    print(x, bool(x))
# break
print("Done")
