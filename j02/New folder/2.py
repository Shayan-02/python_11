a = int(input("number1: "))
b = int(input("number2: "))
max = int()

if a>b:
    max = a
    print(f"{a} is bigger than {b}")
elif b>a:
    max = b
    print(f"{b} is bigger than {a}")
else:
    print(f"{a} = {b}")