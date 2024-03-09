from info import *

p4 = Person(name="reza", pid=0, age=30, tel=0, job="empkoyee")
p4.p_chap()

test1(5, 6)

class Teacher(Person):
    def __init__(self, name, age, year, session):
        super().__init__(name, age)
        self.year = year
        self.session = session

x = Teacher("Mike", "Olsen", 2019, "math")

print(x.name, x.year)