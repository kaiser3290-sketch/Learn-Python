from abc import ABC,abstractmethod 
class Animals(ABC):
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat
        print("i am parent class ANIMAL")

    @abstractmethod
    def display(self):
        print(" i am",self.name,"and i live in ",self.habitat)

class Parrot(Animals):
    def __init__(self,name,habitat):
        print("i am a parrot class constructor")
        super().__init__(name,habitat)

p1=Parrot("Parrot","Tree")
p1.display()