class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I study {self.course}"

st_1 = Student("Farhan", 22, "BSc.CS")
st_2 = Student("Bugembe", 20, "LLb")
st_3 = Student("Lwanga", 25, "BBA")

print(st_1.introduce())
print(st_2.introduce())
print(st_3.introduce())




