number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))

c = number2 ** number1
d = c % number3
number1 -= number2
print(f"{number2} be tavane {number1} hast {c}")
print(f"baghimandeye taghsime {number3} bar {c} hast{d}")
print(f"number1 tagheer karde hast {number1}")