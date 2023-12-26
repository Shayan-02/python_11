import random

# a = ["sang", "kaghaz", "gheichi"]
#
#
#
# for i in range(6):
#     c_r = random.choice(a)
#     print(c_r)


# print(eval(input("enter: ")))
a = []
for _ in range (101):
    x = random.randint(1, 101)
    a.append(x)
sum = 0
for _ in a:
    print(_, end="\t")
print()
for _ in a:
    sum += _

print(sum)