# all the next lines are strings - even char is a string
char = 're'
word = "double quotes work too!"
multi_line_word = """
here come the triple
quotes
"""

'''
print(char)
print(word)
print(multi_line_word)

print(char * 10)
'''
# print(multi_line_word*2 + char*10)

# sinlge line comment
# string slcing
print(word[0:4])
print(word[-4:])
print(word[:-3])
print(word[0:7:3])  # step - means skip for 3 characters after printing from 0
print(word[0:1112:3])

'''
multi line comment
will this work
?
'''

print("multi line comment works bro!")
