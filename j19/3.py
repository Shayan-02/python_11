from tkinter import *


def get_input():
    value = t.get("1.0", "end-1c")
    print(eval(value))


root = Tk()
root.geometry("400x400")

t = Text(root, width = 100, height = 4)
t.pack()
b = Button(root, text="click", command=get_input)
b.pack()
print(type(t))

root.mainloop()
