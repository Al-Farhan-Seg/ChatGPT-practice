class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.__gpa = 0
        self.__email = ""
        self.courses = []  # bi-directional link: list of Course instances

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I study {self.course}"
    
    def set_gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value

    def update_gpa(self, value):
        self.__gpa = value

    def get_gpa(self):
        return self.__gpa
    
    def set_email(self):
        self.__email = f"{self.name}".lower() + ".iuiu.ac@gmail.com"

    def get_email(self):
        return self.__email
    
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
    

# Modelling a relationship between Student and Course
class Course:

    def __init__(self):
        self.__course_name = "Course"
        self.__code = "Code"
        self.__students = []

    def add_student(self, student_obj):
        if student_obj in self.__students:
            return "Student is already enrolled in course"
        else:
            self.__students.append(student_obj)
            #AI gen
            student_obj.add_course(self)
            return True

    def remove_student(self, student_obj):
        self.__students.remove(student_obj)

    def list_students(self):
        print("Student's List".center(50,"_"))
        for i in self.__students:
            print(f"- {i.name}")

    def set_course(self, course_name, code):
        self.__course_name = course_name
        self.__code = code

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
st_1.set_gpa(2.67)

print(st_1.show_profile())

course1 = Course()
course1.set_course("Computer Science", "BSc.CS")
st_1.enroll(course1)
st_1.enroll(course1)

st_2.enroll(course1)
st_3.enroll(course1)

print()
course1.list_students()
course1.remove_student(st_2)
print()
course1.list_students()
