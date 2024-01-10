max1 = 0
max2 = 0
n = int(input("enter count of avgs: "))
for i in range(1, n+1):
    # ids = int(input(f"enter id{i}: "))
    avg = int(input(f"enter avg{i}: "))
    if avg > max1:
        max2 = max1
        max1 = avg
    else:
        if avg > max2:
            max2 = avg

print(max2)