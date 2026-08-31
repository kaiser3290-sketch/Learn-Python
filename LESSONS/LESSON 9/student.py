#Write a program to create a class with name Student and perform the following tasks - Declare a variable grade Print a sentence inside the class Create an object of class student and see the output

class Student:
    def __init__(self):
        self.grade=5
    print("Hello i am a class")
    #creating method
    def show_de(self,name):
        print("I am",name,self.grade)

s1=Student()
s2=Student()
print(s1.grade)
s1.show_de("Himansh")
