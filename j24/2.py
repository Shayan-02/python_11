num1 = int(input("num1: "))
op = input("op: ")
num2 = int(input("num2: "))

try:
    if op == "/":
        print(num1 / num2)
except ZeroDivisionError:
    print("Zero Division Error")
else:
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)

print("done")
