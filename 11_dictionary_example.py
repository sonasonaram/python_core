student_info = {
    'name':'hemanth',
    'location': 'bangalore',
    'age': 27,
    'maritalstatus': 'unmarried',
    'subject': ['English', 'Maths']
}

print(student_info)
print("Name of student is", student_info['name'])
print("Marital Status of student is", student_info['maritalstatus'])


student_info['gender'] = 'male'
print(student_info)


student_info.pop('age')
print(student_info)