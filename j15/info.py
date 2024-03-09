class Person:
    def __init__(self, name="", pid=0, age=0, tel=0, job=""):
        self.name = name
        self.pid = pid
        self.age = age
        self.tel = tel
        self.job = job

    def p_print(self, name, pid, age, tel, job):
        print(name, pid, age, tel, job)
    
    def p_chap(self):
        print(self.name, self.pid, self.age, self.tel, self.job)

p1 = Person("ali", job="student")
print(p1.name, p1.job, p1.age)
p2 = Person()
p2.p_print("reza", 0, 0, 0, "teacher")
p1.p_chap()

class Student(Person):
    def __init__(self, grade, s_id):
        self.grade = grade
        self.s_id = s_id
p3 = Person(name="ahmad", age=20)

def test1(a, b):
    print(a + b)