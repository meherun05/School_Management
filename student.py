from person import Person
from school import School

class Student(Person):
    def __init__(self, name,classRoom):
        super().__init__(name)
        self.classRoom = classRoom
        self.__id = None
        self.marks = {}
        self.subjectGrade  = {}
        self.grade = None

    def finalGrade(self):
        sum = 0
        for grade in self.subjectGrade.values():
            point = School.gradeToValue(grade)
            sum += point
            
        if sum == 0:
            gpa = 0.00
        else:
            gpa = sum / len(self.subjectGrade)
            self.grade = School.valueToGrade(gpa)
        return f'{self.name} Final Grade : {self.grade} with GPA {gpa}'

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id = value