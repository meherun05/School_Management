
class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.subjects = []
        self.students = []

    def addStudent(self,student):
        rollNo = f'{self.name}-{len(self.students)+1}'
        student.id = rollNo
        self.students.append(student)
    
    def addSubject(self,subject):
        self.subjects.append(subject)

    def takeSemisterFinalExam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.finalGrade()
