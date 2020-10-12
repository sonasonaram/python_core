'''
name = input('Enter name: ')
location = input('Enter location: ')
gender = input('Enter gender: ')


print('----- PROFILE ------')
print('Name :', name)
print('Location :', location)
print('Gender :', gender)
print('Summary:', name, 'is a', gender, 'from', location)
'''

'''
fname = input('First Name: ')
lname = input('Last Name: ')
complete_name = fname + ' ' + lname

print(complete_name)
'''

a = 7
b = 5

# addition
print('addition', a + b)

# subtraction
print('subtraction', a - b)

# multiplication
print('multiplication', a * b)

# division
# floor-division
# remainder
if b == 0:
    print("Division not possible")
    print("Floor Division not possible")
    print("Remainder not possible")
else:
    print('division', a / b)
    print('floor division', a // b)
    print('remainder', a % b)

# power
print('to the power', a ** b)



