from school import School
from classRoom import ClassRoom
from person import Person
from student import Student
from teacher import Teacher
from subject import Subject

school = School("ABC",'Dhaka')

seven = ClassRoom("Seven")
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.addClassRoom(seven)
school.addClassRoom(eight)
school.addClassRoom(nine)
school.addClassRoom(ten)

shafin = Student('shafin',ten)
mehrimah = Student('Mehrimah',eight)
meherab = Student('Meherab',eight)
sabrina = Student('Sabrina',nine)

school.studentAddmission(shafin)
school.studentAddmission(mehrimah)
school.studentAddmission(meherab)
school.studentAddmission(sabrina)

meherun = Teacher('Meherun')
shahin = Teacher('Shahin')

bangla = Subject("Bangla",meherun)
Bio = Subject("Bio",meherun)
math = Subject("Math",shahin)
English = Subject("English",shahin)

eight.addSubject(bangla)
eight.addSubject(math)

nine.addSubject(bangla)
nine.addSubject(math)
nine.addSubject(English)

ten.addSubject(bangla)
ten.addSubject(math)
ten.addSubject(English)
ten.addSubject(Bio)

ten.takeSemisterFinalExam()
nine.takeSemisterFinalExam()
eight.takeSemisterFinalExam()

print(school)