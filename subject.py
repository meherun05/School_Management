from person import Person
from school import School

class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.maxMark = 100
        self.passMark = 33

    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluateNumer()
            student.marks[self.name] = mark
            student.subjectGrade[self.name] = School.calculateGrade(mark)

