def maxi(number):
    global max1
    max1 = 0
    if number > max1:
        max1 = number
    return max1

lst = []
for i in range(1, 6):
    a = int(input(f"enter number{i}: "))
    lst.append(a)

for j in lst:
    maxi(j)
    print("max value is :", max1)