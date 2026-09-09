class Sports:
    def play(self):
        print("every sports has its own scoring system")

class Football(Sports):
    def __init__(self):
        self.__score=10
    def showscore(self,newscore):
        self.__score=newscore
        print(self.__score)
    def info(self):
        print("Football score is ")
    def play(self):
        print("in football we have goal scoring system")

class Cricket(Sports):
    def info(self):
        print("Cricket score is ")

footballer=Football()
cricketer=Cricket()

footballer.info()
cricketer.info()
footballer.play()
footballer.showscore(50)