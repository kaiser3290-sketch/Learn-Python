#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class Parrot:
    def __init__(self,name,age):
        #instance variable
        self.name=name
        self.age=age

#creating object
p1=Parrot("Mithu",12)
p2=Parrot("Paa",7)
print(p2.name)