class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.__gpa = 0
        self.__email = ""
        self.courses = []  # bi-directional link: list of Course instances
        #self.__grade = ""

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I study {self.course}"
    
    def update_gpa(self, value):
        value = int(value)
        if 0.0 <= value <= 4.0:
            self.__gpa = value


    def get_gpa(self):
        return self.__gpa
    
    def get_grade(self):
        gpa = self.get_gpa()
        if gpa == 0:
            return f"Grade: F"
        elif 0.0 < gpa <= 1.0:
            return f"Grade: D"
        elif 1.0 < gpa <= 2.0:
            return f"Grade: C"
        elif 2.0 < gpa <= 3.0:
            return f"Grade: B"
        else:
            return f"Grade: A"

    
    def set_email(self):
        self.__email = f"{self.name}".lower() + ".iuiu.ac@gmail.com"

    def get_email(self):
        return f"E-mail: {self.__email}"
    
    def show_profile(self):
        return f"""-----------Student Profile-------------
Name: {self.name}
Age: {self.age}
GPA: {self.get_gpa()}"""
    
    # AI gen
    def add_course(self, course_obj):
        if course_obj in self.courses:
            return False
        self.courses.append(course_obj)
        return True
    
    '''# enroll method to add the current student instance (self) to the course.
    def enroll(self, course_obj):
        course_obj.add_student(self)
        print(course_obj.get_course())'''

    # AI gen
    # enroll method to add the current student instance (self) to the course.
    def enroll(self, course_obj):
        added = course_obj.add_student(self)
        if added:
            print(course_obj.get_course())
        else:
            print(f"{self.name} is already enrolled in {course_obj.get_course()}")

class GraduateStudent(Student):
    def __init__(self, name, age, course, thesis_title, supervisor):
        super().__init__(name, age, course)
        self.thesis_title = thesis_title
        self.supervisor = supervisor
    

# Modelling a relationship between Student and Course
class Course:

    def __init__(self):
        self.__course_name = "Course"
        self.__code = "Code"
        self.__students = []

    def add_student(self, student_obj):
        if len(self.__students) == 30:
            return "Cannot add more than 30 students"
        else:
            if student_obj in self.__students:
                return "Student is already enrolled in course"
            else:
                self.__students.append(student_obj)
                self._txt_write()
                #AI gen
                student_obj.add_course(self)
                return True
            
    # writing the students to a .txt file            
    def _txt_write(self):
        file_path = rf"{self.__course_name}_students_list.txt"

        with open(file_path, "w", newline="") as file:
            for i in self.__students:
                file.write(f"{i.name}\n")
        return file_path

    def remove_student(self, student_obj):
        self.__students.remove(student_obj)
        self._txt_write()

    def list_students(self):
        print("Student's List".center(50,"_"))
        for i in self.__students:
            print(f"- {i.name}")

    def update_course(self, course_name, code):
        self.__course_name = course_name
        self.__code = code
        


    def get_course(self):
        return f"You have enrolled for {self.__course_name} ({self.__code})"



st_1 = Student("Farhan", 22, "BSc.CS")
st_2 = Student("Bugembe", 20, "LLb")
st_3 = Student("Lwanga", 25, "BBA")

st_1.set_email()
print(st_1.get_email())

st_3.__gpa = 2.0
print(st_3.get_gpa())

#print(st_2.__email)
st_1.update_gpa(2.67)
print(st_1.get_grade())
print(st_1.show_profile())
from time import sleep

sleep(5)
course1 = Course()
course1.update_course("Computer Science", "BSc.CS")
st_1.enroll(course1)
st_1.enroll(course1)

st_2.enroll(course1)
st_3.enroll(course1)

print()
course1.list_students()
course1.remove_student(st_2)
print()
course1.list_students()
