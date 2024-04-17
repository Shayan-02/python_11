from tkinter import *


win = Tk()
win.geometry("700x300")


def get_input():
    value = my_text_box.get("1.0", "end-1c")
    print(value)


# Creating a text box widget
my_text_box = Text(win, height=5, width=40)
my_text_box.pack()

# Create a button for Comment
comment = Button(win, height=5, width=10, text="Comment", command=lambda: get_input())

# command=get_input() will wait for the key to press and displays the entered text
comment.pack()

win.mainloop()
