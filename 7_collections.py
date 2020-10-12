# list - mutable, can contain duplicate elements, ordered

studentL = ['hemanth', 'kumar', 'rakesh', 'vijay', 'kalyan', 'raj', 'rahul']

total_students = len(studentL)
print("We have", total_students, "students")

studentL.sort()
print("The sorted list of students is", studentL)

studentL.append('yana')
print("a new student yana joined the class, now the list is:", studentL)

studentL.remove('kumar')
studentL.remove('vijay')
print("kumar and vijay left the class, now the list is:", studentL)

studentL.pop(3)
print("the 3rd student has left the class, now the list is:", studentL)

new_students = ['ganesh', 'durgesh', 'ramesh']
print("new students have arrived, they need to put in class. The list of new students is:", new_students)

studentL.extend(new_students)
print("Now the class is:", studentL)

studentL.sort()
print("Once again sorted list:", studentL)

studentL.reverse()
print("Reverse sorting:", studentL)



# tuple - immutable, can contain duplicate elements, ordred

studentT = ('vishal', 'sunil', 'raghu')
print("The student tuple:", studentT)

no_of_hemanths = studentT.count('hemanth')
print("Total number of hemanths is", no_of_hemanths)

studentL.extend(studentT)
print("Updated student list:", studentL)



# set - mutable, cannot contain duplicate elements, unordered

studentS = {'Babu', 'Patel', 'Kohli', 'Babu', 'himesh', 'Patel'}
print("student set:", studentS)

studentS.pop()
print("Now set looks like:", studentS)

studentS.discard('Babu')                   # discard does not throw error for missing item, remove does
print("new set situation:", studentS)

studentS.add('Science')
print("new set", studentS)

studentS.update(studentT)
print('updated set', studentS)




# dictionary -- keyvalue pair, advanced set