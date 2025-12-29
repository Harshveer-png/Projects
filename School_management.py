# Here is the code for the School_management 
class Student:
    def __init__ (self,name,roll_number,Batch):
        self.name = name
        self.roll_number = roll_number
        self.Batch = Batch


    def show_details (self):
        print(self.name, self.roll_number, self.Batch)

class Teacher:
    def __init__ (self, name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = subject

    def show_details(self):
        print(self.name, self.salary, self.subject)

class School:
    def __init__ (self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, students):
        self.students.append(students)

    def add_teacher (self, teachers):
        self.teachers.append(teachers)


    def show_all_students(self):
        for stu in self.students:
            stu.show_details()


    def show_all_teachers(self):
        for tec in self.teachers:
            tec.show_details()



school = School("PIT")
s1 = Student("Harshveer Kumar", 33 , "3A19")
s2 = Student("Chandraveer", 63, "3A19")

t1 = Teacher("Umesh Kumar Singh" , 1000000,"relation")
t2 = Teacher("Rinku singh", 100000000, "love for a family")


school.add_student(s1)
school.add_student(s2)

school.add_teacher(t1)
school.add_teacher(t2)


school.show_all_students()
school.show_all_teachers()



