from tkinter import *

root = Tk()
root.title('test page')
root.resizable(False, False)
root.geometry("500x500")
root.config(bg="lightgreen")
lbl_name = Label(root, text="name", fg="blue", font=(25), bg="lightgreen").pack()
lbl_lname = Label(root, text="lname").pack()
root.mainloop()