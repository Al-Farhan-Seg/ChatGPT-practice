import os, json
class Student:
    total_students = 0  # class variable shared across all instances

    # setting the e-mail of the current Student instance {since it is private}
    def set_email(self):
        name = self.name
        name = name.replace(" ", "")
        self.__email = f"{name}".lower() + ".iuiu.ac@gmail.com"
        return self.__email

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__gpa = 0
        self.__email = self.set_email()
        self.__courses = []  # full Course_obj
        self.__grades = [] # {Course.__course_name : grade}
        Student.total_students += 1  # increment every time a new Student is created

    @classmethod
    def get_total_students(cls):
        return f"Total Students Created: {cls.total_students}"
    
    # setting and updating the GPA of the current Student instance
    def update_gpa(self):
        total_gpcu = 0
        total_cu = 0
        gpa = 0

        for i in self.__grades:
            
            for k,v in i.items():
                if 0 <= v < 60:
                    grade_point = 0.0
                elif 60 <= v < 70:
                    grade_point = 1.0
                elif 70 <= v < 75:
                    grade_point = 2.0
                elif 75 <= v < 80:
                    grade_point = 2.5
                elif 80 <= v < 85:
                    grade_point = 3.0
                elif 85 <= v < 90:
                    grade_point = 3.5
                elif 90 <= v < 101:
                    grade_point = 4.0
                for course in self.__courses:
                    if course._Course__course_name == k:
                        credit_units = course._Course__credit_units
                        total_cu += credit_units
                        gpcu = credit_units * grade_point
                        total_gpcu += gpcu

        
        gpa = total_gpcu / total_cu
        self.__gpa = gpa
        return "GPA calculated and updated"


    # returning the GPA of the current Student instance
    def get_gpa(self):
        return self.__gpa
    
    # returning the particular GRADE of the current Student instance in relation to it's GPA
    def get_grade(self, course_obj):
        if course_obj not in self.__courses:
            return f"{self.name} is not enrolled for {course_obj._Course__course_name}"
        else:
            for i in self.__grades:
                for k,v in i.items():
                    if k == course_obj._Course__course_name:
                        mark = v
                        if 0 <= v < 60:
                            grade_point = 0.0
                            rank = "F"
                        elif 60 <= v < 70:
                            grade_point = 1.0
                            rank = "D"
                        elif 70 <= v < 75:
                            grade_point = 2.0
                            rank = "C"
                        elif 75 <= v < 80:
                            grade_point = 2.5
                            rank = "C+"
                        elif 80 <= v < 85:
                            grade_point = 3.0
                            rank = "B"
                        elif 85 <= v < 90:
                            grade_point = 3.5
                            rank = "B+"
                        elif 90 <= v < 101:
                            grade_point = 4.0
                            rank = "B"
                        break
        return f"""Student: {self.name}
Course: {course_obj._Course__course_name}
Grade: {mark}
Grade Point: {grade_point}
Rank: {rank}"""
    
    def average_mark(self):
        total = 0
        num = 0
        for i in self.__grades:
            for k,v in i.items():
                total += v
                num += 1
        average = total / num

        return F"Average Mark: {average}"

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
            course_obj.add_student(self)
            return True
    
    def remove_course(self, course_obj):
        if course_obj in self.__courses:
            self.__courses.remove(course_obj)
            course_obj.remove_student(self)
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
        self.__thesis_stage = "Not-Set"
        self.supervisor = supervisor

        # Add-on: Let GraduateStudent override show_profile() to include thesis and supervisor.
    def show_profile(self):
        return f"""-----------Student Profile-------------
Name: {self.name}
Age: {self.age}
GPA: {self.get_gpa()}
Thesis: {self.thesis_title}
Thesis Stage: {self.__thesis_stage}
Supervisor: {self.supervisor}"""
    
    def set_thesis_stage(self):
        attempts = 0
        while attempts < 3:
            try:
                choice = int(input("""_____________THESIS STAGE_____________
        Choose a stage for the Thesis:
                1. Pending
                2. Defended
                3. Approved
                """))
                if choice == 1:
                    self.__thesis_stage = "Pending"
                elif choice == 2:
                    self.__thesis_stage = "Defended"
                elif choice == 3:
                    self.__thesis_stage = "Approved"
            except ValueError:
                print("Please enter only an INTEGER as choice")
        return "Too many failed attempts"
    

    

# Modelling a relationship between Student and Course
class Course:
    total_courses = 0

    def __init__(self):
        self.__course_name = "Course"
        self.__code = "Code"
        self.__credit_units = 0
        self.__students = [] # full Student_obj
        self.__instructors = [] # only "Instructor_obj.name"
        self.__grades = [] # {Student_obj.name : grade}
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

        for i in self.__grades:
            for k,v in i.items():
                if k == student_obj.name:
                    pair = {self.__course_name : v}
                    student_obj._Student__grades.remove(pair) # concurrently remove this grade from Student's self.__grades
        self._json_write()
    

    # returning the "name" of Student instances that have enrolled for the current Course instance
    def list_students(self):
        print("Student's List".center(50,"_"))
        for i in self.__students:
            print(f"- {i.name}")

    def update_course(self, course_name, code, credit_units):
        self.__course_name = course_name
        self.__code = code
        self.__credit_units = credit_units
        self._json_write()
        
   
    def get_course(self):
        return f"You have enrolled for {self.__course_name} ({self.__code})"
    
    def add_instructor(self, instructor_obj):
        if len(self.__instructors) == 3:
            return "Cannot add more than 3 instructors for a course"
        else:
            
            if instructor_obj.name in self.__instructors:
                return "Instructor already assigned to course"
            else:
                self.__instructors.append(instructor_obj.name)
                self._json_write()
                return f"{instructor_obj.name} successfully assigned to {self.__course_name}({self.__code})"


    def add_grades(self, student_obj, grade):
        if student_obj not in self.__students:
            return f"{student_obj.name} is not registered for this course"
        else:
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

        file = {
            "Course Name": self.__course_name,
            "Code": self.__code,
            "Credit Units": self.__credit_units,
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

class Instructor:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


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
                return f"{course_obj._Course__course_name} already registered to {self.name}"
            else:
                self.courses.append(course_obj)
                self.uni_json_write()
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
                self.uni_json_write()
                return f"{student_obj.name} successfully registered to {self.name}"
            
            
    def uni_json_write(self):
        top_file = {
            "University" : self.name,
            "Courses" : [],
            "Students": []
        }

        courses_list = []
        #Course_logic
        for i in self.courses:
            students = []

            courses_file = {
            "Course_name" : i._Course__course_name,
            "Code" : i._Course__code,
            "Credit Units" : i._Course__credit_units,
            "Instructors" : i._Course__instructors,
            "Students" : [],
        }
            for stu in i._Course__grades:
                students.append(stu)
            courses_file["Students"] = students
            courses_list.append(courses_file)
            
        top_file["Courses"] = courses_list

        students_list = []
        for j in self.students:


            student_file = {
                "Name" : j.name,
                "Age" : j.age,
                "E-mail" : j._Student__email,
                "Courses" : [],
                "Grades" : []
            }
            courses = []
            grades = []
            for i in j._Student__courses:
                courses.append(i._Course__course_name)
            student_file["Courses"] = courses
            for i in j._Student__grades:
                grades.append(i)
            student_file["Grades"] = grades

            students_list.append(student_file)
        top_file["Students"] = students_list



        filepath = rf"{self.name}_data.json"
        with open(filepath, "w") as uni_data:
            content = json.dump(top_file, uni_data, indent=3)
