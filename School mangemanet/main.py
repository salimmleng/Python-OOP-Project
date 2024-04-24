from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School('ABC','Dhaka')

eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

# adding classroom

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student

rana = Student('Rana',eight)
korim = Student('Korim',nine)
fahim = Student('Fahim',ten)
hamim = Student('Hamim',ten)

school.student_admission(rana)
school.student_admission(korim)
school.student_admission(fahim)
school.student_admission(hamim)

# adding teachers

abul = Teacher('Abul khan')
babul = Teacher('Babul khan')
kabul = Teacher('Kabul khan')

# adding subjects

bangla = Subject('Bangla',abul)
physics = Subject('Physics',babul)
chemistry = Subject('Chemistry',kabul)
biology = Subject('Biology',kabul)

eight.add_subject(bangla)                   
eight.add_subject(physics)                   
eight.add_subject(chemistry)                   
nine.add_subject(biology)                   
nine.add_subject(physics)                   
nine.add_subject(chemistry)                   
ten.add_subject(chemistry)                   
ten.add_subject(physics)                   
ten.add_subject(bangla)                   
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)


