from person import Person
import random

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def evaluateNumer(self):
        return random.randint(50,100)