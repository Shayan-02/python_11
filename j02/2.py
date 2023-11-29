n1 = int(input("enter number1: "))
op = input("enter the operation: ")
n2 = int(input("enter number2: "))

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2}")

if op == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif op == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif op == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("invalid operation")