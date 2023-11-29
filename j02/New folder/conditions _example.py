# fib
# 1 1 2 3 5 8 13 21 ...
f1 = 1
f2 = 1
n = int(input("Enter a number: "))
if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
else:
    print(f1, f2, end = " ", sep=" ")
    i = 3
    while i <= n:
        f3 = f1 + f2
        print(f3, end = " ")
        f1 = f2
        f2 = f3
        i += 1