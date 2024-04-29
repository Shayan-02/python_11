from tkinter import *


def new_tab():
    window = Tk()
    window.mainloop()

root = Tk()


btn = Button(root, text="Click me", command = new_tab)
btn.pack()

root.mainloop()