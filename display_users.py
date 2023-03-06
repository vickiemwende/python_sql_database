from main import Student

Students = Student.select()
for Student in Students:
    print(Student.stud_name, Student.stud_email, Student.stud_password)