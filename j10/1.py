def sums(a, b):
    c = a + b
    d = a * b
    return d
n = input("op: ")
if n == "-":
    pass
elif n == "+":
    sums(5, 6)
else:
    print(2*sums(5, 6))

