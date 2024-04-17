from tkinter import *

def get_full_name():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    full_name = f"{first_name} {last_name}"
    full_name_label.config(text=f"Full Name: {full_name}")


window = Tk()
window.title("Full Name App")

first_name_label = Label(window, text="First Name:")
first_name_label.grid(row=0, column=0)

first_name_entry = Entry(window)
first_name_entry.grid(row=0, column=1)

last_name_label = Label(window, text="Last Name:")
last_name_label.grid(row=1, column=0)

last_name_entry = Entry(window)
last_name_entry.grid(row=1, column=1)

get_full_name_button = Button(window, text="Get Full Name", command=get_full_name)
get_full_name_button.grid(row=2)

full_name_label = Label(window, text="")
full_name_label.grid(row=3)

window.mainloop()
