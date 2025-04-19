
class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.classRoom = {}
        self.teachers = {}

    def addClassRoom(self,classRoom):
        self.classRoom[classRoom.name] = classRoom

    def addTeacher(self,subject,teacher):
        self.teachers[subject] = teacher

    def studentAddmission(self,student):
        className = student.classRoom.name
        self.classRoom[className].addStudent(student)

    @staticmethod
    def calculateGrade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks >= 70 and marks < 80:
            return "A"
        elif marks >= 60 and marks < 70:
            return "A-"
        elif marks >= 50 and marks < 60:
            return "B"
        elif marks >= 40 and marks < 50:
            return "C"
        elif marks >= 33 and marks < 40:
            return "D"
        else :
            return "F"
        
    @staticmethod
    def gradeToValue(grade):
        gradeMap = {
            'A+' : 5.00,
            'A'  : 4.00,
            'A-' : 3.50,
            'B'  : 3.00,
            'C'  : 2.00,
            'D'  : 1.00,
            'F'  : 0.00
        }
        return gradeMap[grade]
    
    @staticmethod
    def valueToGrade(value):
        if value >= 4.5 and value <= 5.00:
            return "A+"
        elif value >= 3.5 and value < 4.5:
            return "A"
        elif value >= 3.0 and value < 3.5:
            return "A-"
        elif value >= 2.5 and value < 3.0:
            return "B"
        elif value >= 2.0 and value < 2.5:
            return "C"
        elif value >= 1.0 and value < 2.0:
            return "D"
        else :
            return "F"
        
    def __repr__(self):
        for key,value in self.classRoom.items():
            print(key)
        print('All students')
        result= ''
        for key,value in self.classRoom.items():
            result += f'---{key.upper()} class room students\n'
            for val in value.students:
                result +=f'{val.name}\n'
        print(result)
        print('All Subjects')
        subject= ''
        for key,value in self.classRoom.items():
            subject += f'---{key.upper()} class room subjects\n'
            for sub in value.subjects:
                subject +=f'{sub.name}\n'
        print(subject)
        print('All Teachers')
        teacher = ''
        for key, value in self.classRoom.items():
            teacher += f'---{key.upper()} class room teachers\n'
            for sub in value.subjects:
                teacher += f'{sub.teacher.name} (Subject: {sub.name})\n'
            if not value.subjects:
                teacher += 'No teachers assigned\n'
        print(teacher)
        print("Students result")
        for key ,value in self.classRoom.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subjectGrade[k])
                print(student.finalGrade())
        return ''
    
