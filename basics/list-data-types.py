data_types = [
    # this can span multiple lines
    2,
    4 + 5j,  # thats right! i support complex numbers too
    'hello',
    '',
    True,  # notice the caps here shiva
    None,
    [
        "yes",
        # data_types] - this wont be a circular reference - but a undefined var in local
        2]
]
for x in data_types:
    print(type(x), x)
