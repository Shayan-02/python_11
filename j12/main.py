class Person:
    x = 50
    def __init__(self, name, age, p_id):
        self.name = name
        self.age = age
        self.p_id = p_id
    def sleep(self):
        print(self.name, "sleeping...")
    def eat(self):
        print(self.name, "eating...")

class Student(Person):
    def __init__(self, st_id, avg, degree, major):
        self.st_id = st_id
        self.avg = avg
        self.degree = degree
        self.major = major

s1 = Student(24, 17.5, "bd", "computer" )
s1.name = "alireza ahmadi"
print(s1.name)
s1.sleep()