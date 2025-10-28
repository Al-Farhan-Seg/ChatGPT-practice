import os, json
class Student:
    total_students = 0  # class variable shared across all instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__gpa = 0
        self.__email = ""
        self.__courses = []  # bi-directional link: list of Course instances
        self.__grades = []
        Student.total_students += 1  # increment every time a new Student is created

    @classmethod
    def get_total_students(cls):
        return f"Total Students Created: {cls.total_students}"

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old"
    
    # setting and updating the GPA of the current Student instance
    def update_gpa(self, value):
        value = int(value)
        if 0.0 <= value <= 4.0:
            self.__gpa = value

    # returning the GPA of the current Student instance
    def get_gpa(self):
        return self.__gpa
    
    # returning the particular GRADE of the current Student instance in relation to it's GPA
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

    # setting the e-mail of the current Student instance {since it is private}
    def set_email(self):
        self.__email = f"{self.name}".lower() + ".iuiu.ac@gmail.com"

    # returning the e-mail of the current Student instance
    def get_email(self):
        return f"E-mail: {self.__email}"
    
    # Display the profile of the current Student {undergraduate}
    def show_profile(self):
        emp = []
        for i in self.courses:
            # to show courses enrolled for by Student
            emp.append(i._Course__course_name)
        return f"""-----------Student Profile-------------
Name: {self.name}
Age: {self.age}
GPA: {self.get_gpa()}
Courses: {emp}"""
        
    
    # AI gen(now is understood)
    # adding the 'given' Course object to the 'self.courses' list of the current Student instance
    def add_course(self, course_obj):
        if course_obj in self.__courses:
            return False
        else:
            self.__courses.append(course_obj)
            return True
    
    def remove_course(self, course_obj):
        if course_obj in self.__courses:
            self.__courses.remove(course_obj)
            return True
        else:
            return False

    # AI gen (now is understood)
    # enroll method to add the current student instance (self) to the course.
    def enroll(self, course_obj):
        result = course_obj.add_student(self)
        if result == True:
            print(course_obj.get_course())
        else:
            print(result)

    def list_courses(self):
        if len(self.__courses) <= 0:
            return "No courses enrolled for yet"
        else:
            for i in self.__courses:
                return i._Course__course_name


class GraduateStudent(Student):
    def __init__(self, name, age, thesis_title, supervisor):
        super().__init__(name, age)
        self.thesis_title = thesis_title
        self.supervisor = supervisor

        # Add-on: Let GraduateStudent override show_profile() to include thesis and supervisor.
    def show_profile(self):
        return f"""-----------Student Profile-------------
Name: {self.name}
Age: {self.age}
GPA: {self.get_gpa()}
Thesis: {self.thesis_title}
Supervisor: {self.supervisor}"""
    

# Modelling a relationship between Student and Course
class Course:
    total_courses = 0

    def __init__(self):
        self.__course_name = "Course"
        self.__code = "Code"
        self.__students = []
        self.__instructors = []
        self.__grades = []
        Course.total_courses += 1

    # adding the Student instance to the STYDENT'S LIST of the Course instance
    def add_student(self, student_obj):
        if len(self.__students) == 30:
            return "Cannot add more than 30 students"
        else:
            if student_obj in self.__students:
                return f"{student_obj.name} is already enrolled in {self.__course_name}"
            else:
                self.__students.append(student_obj)
                self._json_write()
            
                #AI gen (now is understood)
                # add the current Course instance to the list of courses for the given Student object
                student_obj.add_course(self)
                return True
            
    # writing the Student instances that have enrolled for the Course instance to a .txt file
    def _txt_write(self):
        file_path = rf"{self.__course_name}_students_list.txt"

        with open(file_path, "w", newline="") as file:
            for i in self.__students:
                file.write(f"{i.name}\n")
        return file_path

    #removing the Student instance from the STYDENT'S LIST of the Course instance
    def remove_student(self, student_obj):
        self.__students.remove(student_obj)
        student_obj.remove_course(self)
        self._json_write()
    

    # returning the "name" of Student instances that have enrolled for the current Course instance
    def list_students(self):
        print("Student's List".center(50,"_"))
        for i in self.__students:
            print(f"- {i.name}")

    def update_course(self, course_name, code):
        self.__course_name = course_name
        self.__code = code
        self._json_write()
        
   
    def get_course(self):
        return f"You have enrolled for {self.__course_name} ({self.__code})"
    
    def add_instructor(self):
        if len(self.__instructors) == 3:
            return "Cannot add more than 3 instructors for a course"
        else:
            attemmpts = 0
            while attemmpts < 3:
                name = input("Enter name of new instructor: ")
                name = name.strip()
                name = name.upper()
                if name in self.__instructors:
                    print("Instructor already assigned to course")
                    attemmpts += 1
                else:
                    self.__instructors.append(name)
                    self._json_write()
                    return f"{name} successfully assigned to {self.__course_name}({self.__code})"


    def add_grades(self, student_obj, grade):
        if grade in range(0, 101):
            for i in self.__grades:
                for k,v in i.items():
                    if student_obj.name == k:
                        pair = {student_obj.name : i[student_obj.name]}
                        attempts = 0
                        while attempts < 3:
                            query = input(f"Grade for {student_obj.name} available. Do you want to update it ? (Yes or No)")
                            query = query.upper()

                            if query[0] == "N":
                                return f"Grade for {student_obj.name} not updated"
                            elif query[0] == "Y":
                                self.__grades.remove(pair)
                                student_obj._Student__grades.remove({self.__course_name : pair[student_obj.name]})

                                self.__grades.append({student_obj.name : grade})
                                student_obj._Student__grades.append({self.__course_name : grade})
                                self._json_write()
                                return f"Grade for {student_obj.name}  successfully updated"
                            else:
                                print("Wrong choice made..........TRY AGAIN")
                                attempts += 1
                        return "Too many wrong attempts"
                #break

            self.__grades.append({student_obj.name : grade})
            student_obj._Student__grades.append({self.__course_name : grade})
            self._json_write()
            return f"Grade for {student_obj.name} has been successfully added"
        else:
            return f"Grade must be between 0 to 100"
                

    def _json_write(self):
        # Coursenamme
        #coresecode 
        # instructors : []
        #students : [{name: NAME,
        #             ]


        file = {
            "Course Name": self.__course_name,
            "Code": self.__code,
            "Instructors": self.__instructors,
            "Students": []
        }

        student_json_list = []
        
        #very well understood
        for student in self.__students:
            grade = None
            for i in self.__grades:
                if student.name in i:
                    grade = i[student.name]
                    break
            student_json_list.append({"Name":student.name, "Age":student.age, "Grade":grade})

        file["Students"] = student_json_list

        file_path = rf"{self.__course_name}_data.json"

        with open(file_path, "w") as json_file:
            data = json.dump(file, json_file, indent=3)


class University:

    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        
    def add_course(self, course_obj):
        if not isinstance(course_obj, Course):
            print("REGISTRATION FAILED")
            return "Please enter a COURSE to add to the University"
        else:
            if course_obj in self.courses:
                return f"{course_obj._Course__course_name}already registered to {self.name}"
            else:
                self.courses.append(course_obj)
                return f"{course_obj._Course__course_name} successfully registered to {self.name}"
            
    def add_student(self, student_obj):
        if not isinstance(student_obj, Student):
            print("REGISTRATION FAILED")
            return "Please enter a STUDENT to add to the University"
        else:
            if student_obj in self.students:
                return f"{student_obj.name} already registered to {self.name}"
            else:
                self.students.append(student_obj)
                return f"{student_obj.name} successfully registered to {self.name}"
