import time

f = open('test.txt', 'w')

try:
    for x in range(20):
        time.sleep(1)
        f.write(str(x) + '\n')
finally:
    print("Finally...")
    f.close()

print("letz go hofcm")
