class Demo:
    def __check(self):
        return "Demo's check"
    def display(self):
        print(self.check())

class Demo_Drived(Demo):
    def __check(self):
        return "Demo's Drived's check"

Demo().display()
Demo_Drived().display()