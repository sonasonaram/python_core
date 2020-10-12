# we have a list of students
# if there is a student, who did not pay, we want to get the names
# else we are okay


def identify_students_who_did_not_pay(list_of_students):
    non_payment_student_names = []
    for student_info in list_of_students:
        if student_info['payment'] == False:
            non_payment_student_names.append(student_info['name'])

    return non_payment_student_names




list_of_students = [

    {'name': 'Diksha', 'payment': False},
    {'name': 'Hemanth', 'payment': True},
    {'name': 'Rahul', 'payment': False}
]

non_pmt_list = identify_students_who_did_not_pay(list_of_students)

print(non_pmt_list)

