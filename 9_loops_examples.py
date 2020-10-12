list_of_students = ['hemanth', 'kumar', 'rakesh', 'vijay', 'kalyan', 'raj', 'rahul', 'priya', 'harsh']
list_of_attendees = [True,      True,    False,    True,    True,     False, True,    False,   False  ]

'''
total_students = len(list_of_students)

for i in range(total_students):
    if list_of_attendees[i] == True:
        print (list_of_students[i], 'is present')
    else:
        print(list_of_students[i], 'is absent')
'''

# make a list with all the student names reversed

list_of_reverse_student_names = []

for name in list_of_students:
    reverse_name = ''            # reverse_name: is a blank variable
    for i in range(len(name) - 1, -1, -1):   # running a loop from 6, 5, 4, 3, 2, 1,0
        reverse_name = reverse_name + name[i]   # taking each of the letters from back to front and adding to reverse_name variable
    list_of_reverse_student_names.append(reverse_name)

print (list_of_students)
print (list_of_reverse_student_names)


# easily

list_of_reverse_student_names2 = []
for name in list_of_students:
    list_of_reverse_student_names2.append(name[::-1])

print (list_of_reverse_student_names2)