from tkinter import *


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(
            width=17, textvariable=self.equation, bg="#fff", font=("Arial Bold", 28)
        ).place(x=0, y=0)
        Button(
            text="(",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("("),
        ).place(x=0, y=50)
        Button(
            text=")",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(")"),
        ).place(x=90, y=50)
        Button(
            text="%",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("%"),
        ).place(x=180, y=50)
        Button(
            text="1",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(1),
        ).place(x=0, y=125)
        Button(
            text="2",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(2),
        ).place(x=90, y=125)
        Button(
            text="3",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(3),
        ).place(x=180, y=125)
        Button(
            text="4",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(4),
        ).place(x=0, y=200)
        Button(
            text="5",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(5),
        ).place(x=90, y=200)
        Button(
            text="6",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(6),
        ).place(x=180, y=200)
        Button(
            text="7",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(7),
        ).place(x=0, y=275)
        Button(
            text="8",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(8),
        ).place(x=180, y=275)
        Button(
            text="9",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(9),
        ).place(x=90, y=275)
        Button(
            text="0",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show(0),
        ).place(x=90, y=350)
        Button(
            text=".",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("."),
        ).place(x=180, y=350)
        Button(
            text="+",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("+"),
        ).place(x=270, y=275)
        Button(
            text="-",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("-"),
        ).place(x=270, y=200)
        Button(
            text="/",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("/"),
        ).place(x=270, y=50)
        Button(
            text="x",
            width=11,
            height=4,
            relief="flat",
            bg="white",
            command=lambda: self.show("*"),
        ).place(x=270, y=125)
        Button(
            text="=",
            width=11,
            height=4,
            relief="flat",
            bg="lightgreen",
            command=lambda: self.solve(),
        ).place(x=270, y=350)
        Button(
            text="c", width=11, height=4, relief="flat", command=lambda: self.clear()
        ).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        resault = eval(self.entry_value)
        self.equation.set(resault)


root = Tk()


calculator = Calculator(root)


root.mainloop()

