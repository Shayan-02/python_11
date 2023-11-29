f1 = 1
f2 = 1
f3 = f1 + f2
f4 = f2 + f3
n = int(input("Enter a number: "))
if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
elif n == 3:
    print(f1, f2, end=" ", sep=" ")
    print(f3, end=" ")
elif n == 4:
    print(f1, f2, f3, f4, sep=" ")