list_of_student_info = [
    {'name': 'hemanth', 'location': 'bangalore', 'age': 27, 'maritalstatus': 'unmarried'},
    {'name': 'kumar',   'location': 'mysuru',    'age': 32, 'maritalstatus': 'married'},
    {'name':'ganesh',   'location': 'hyderabad', 'age': 25, 'maritalstatus': 'unmarried'}
]

for student_info in list_of_student_info:
    print("Student name:", student_info['name'])
    if student_info['maritalstatus'] == 'married':
        print(student_info['name'], "is married")


