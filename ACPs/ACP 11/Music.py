class Instruments():
    def __init__(self,name):
        self.name=name
        print(self.name)

class Synthesizer(Instruments):
    def __init__(self,name):
        super().__init__(name)

class Guitar(Instruments):
    def __init__(self,name):
        super().__init__(name)

class Tabla(Instruments):
    def __init__(self,name):
        super().__init__(name)

s1=Synthesizer("Synthesizer")
g1=Guitar("Guitar")
t1=Tabla("Tabla")