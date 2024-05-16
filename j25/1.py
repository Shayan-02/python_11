def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value, end= " ")


def simpleGeneratorFun2():
    return 1, 2, 3

for value in simpleGeneratorFun2():
    print(value * 2, end=" ")
