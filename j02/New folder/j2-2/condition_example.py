a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))
max = 0

# if a > b:
#     max = a
# elif a > c:
#     max = a
# elif b > a:
#     max = b
# elif b > c:
#     max > b
# elif c > a:
#     max = c
# elif c > b:
#     max = c
# print(max)

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > a and c > b:
    max = c
print(f"max of {a} and {b} and {c} is {max}")