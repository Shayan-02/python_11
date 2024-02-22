class Test:
    x = 50
    def __init__(self, name, p_id, age):
        self.name = name
        self.p_id = p_id
        self.age = age
    def print_age(self):
        print(f"hi {self.age}")

t1 = Test("ali", 253698, 20)
print(t1.x)
