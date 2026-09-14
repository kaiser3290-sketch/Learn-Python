class Pet:
    def __init__(self):
        print("I have my own food")

class Dog:
    def __init__(self):
        self.__food="Dog food"  
    def showfood(self,newfood):
        self.__food=newfood
    def info(self,food):
        print("my food is ",food)
    def play(self):
        print("we dog eat food by mouth")

d=Dog()

d.info("Doog fod")
d.play()
d.showfood("Doog fod")