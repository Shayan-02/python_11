n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter 3th number: "))
n4 = int(input("enter 4th number: "))

avg = (n1 + n2 + n3 + n4)/4
if n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0 or n1 > 20 or n2 > 20 or n3 > 20 or n4 > 20:
    print("invalid number...")
elif avg >= 18:
    print(f"your avg is: {avg} so your avg is A")
elif avg >= 16:
    print(f"your avg is: {avg} so your avg is B")
elif avg >= 14:
    print(f"your avg is: {avg} so your avg is C")
elif avg >= 12:
    print(f"your avg is: {avg} so your avg is D")
elif avg >= 10:
    print(f"your avg is: {avg} so your avg is E")
elif avg < 10:
    print(f"your avg is: {avg} so you failed")
