from tkinter import *


def show_full_name():
    firstname = firstnameent.get()
    lastname = lastnameent.get()
    fullname = fullnamelbl.config(text=f"fullname:{firstname} {lastname}")


root = Tk()
root.title("full name app")
root.geometry("400x400")

firstnamelbl = Label(root, text="first name : ", font=("arial", 15, "bold"))
firstnamelbl.place(x=5, y=10)
lastnamelbl = Label(root, text="first name : ", font=("arial", 15, "bold"))
lastnamelbl.place(x=5, y=80)

firstnameent = Entry(root, width=20, font=("arial", 15, "bold"))
firstnameent.place(x=130, y=15)
lastnameent = Entry(root, width=20, font=("arial", 15, "bold"))
lastnameent.place(x=130, y=80)

submit = Button(
    root, text="full name", font=("arial", 15, "bold"), command=show_full_name
)
submit.place(x=150, y=180)

fullnamelbl = Label(root, text="", font=("arial", 15, "bold"))
fullnamelbl.place(x=5, y=250)

root.mainloop()
