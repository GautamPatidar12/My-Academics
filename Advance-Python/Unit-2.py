'''
# Object Oriented Program

#1 First program class syntax
class MyFirstProgram:
    c="Gautam Patidar"
    print("Welcome to Object-Oriented Programming")

a=MyFirstProgram()
print(a)
print(a.c)


#2 Making multiple objects with same class
class Multiple_Objects:
    a=10
    b=20.5
    c="Gautam Patidar"
    print("Welcome to Object-Oriented Programming")

p=Multiple_Objects()
q=Multiple_Objects()

print(p)
print(q.a,q.b)


# Print student details using class and object
class Student:
    def details(self, name, clas, subject):
        print("Name: ", name)
        print("Class: ", clas)
        print("Subject: ", subject)

name = "Gautam Patidar"
clas = "Btech CSIT"
subject = "Advanced Python"

x = Student()

x.details(name, clas, subject)


'''



class Student:
    def details(self, name, clas, subject):
        print("Name: ", name,"   Class: ", clas,"   Subject: ", subject)
        #print("Name: ", name)
        #print("Class: ", clas)
        #print("Subject: ", subject)

name = ["Gautam Patidar","Tanmay Kaushal", "Arun Malviya","Aashutosh Kumar Singh"]
clas = ["Btech CSIT","Btech CSIT","Btech CSIT","Btech CSIT"]
subject = ["Advanced Python","Mathematics","Digital Electroncis","Computer Architecture"]

x = Student()

for i in range(4):
    x.details(name[i], clas[i], subject[i])