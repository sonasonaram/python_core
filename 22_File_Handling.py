myfile = open('D:/dog cat.txt', 'r')
print(myfile.read(10))
print(myfile.readline())

myfile = open('D:/dog cat.txt', 'r')
counter = 0
for line in myfile:
    counter = counter + 1
print("Number of lines", counter)


myfile = open('D:/dog cat.txt', 'w')
myfile.write('Dogs are dancing')
myfile.close()

myfile = open('D:/hemanthfile.txt', 'x')

myfile = open('D:/hemanthfile.txt', 'a')
myfile.write("This is hemanth session")
myfile.close()

import os
try:
    os.remove('D:/hemanthfile.txt')
except:
    print("File not present to be deleted")


# os.makedirs('D:/hemanthfolder')
# myfile = open('D:/hemanthfolder/hemanth.txt', 'a')
# myfile.write("This is hemanth session")
# myfile.close()

os.remove('D:/hemanthfolder/hemanth.txt')
os.rmdir('D:/hemanthfolder')