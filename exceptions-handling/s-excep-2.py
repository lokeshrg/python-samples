def create_emp(name, age):
    if age > 100:
        raise ValueError("AgeError", 'Age beyond limit')
    pass
    print('Employee created!')

create_emp('ko', 100)
create_emp('tokka', 102)
create_emp('pakka', 99)