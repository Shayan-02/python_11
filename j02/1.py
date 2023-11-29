fname = input("your first name: ")
lname = input("your last name: ")

print("your firstname is: ", fname, "and your lastname is: ", lname, "and your fullname is: ", fname, lname)
print(f"your firstname is: {fname} and your lastname is: {lname} and your fullname is {fname} {lname}")
print(f"your firstname is: {fname} and your lastname is: {lname} and your fullname is {4*5}")
print("your firstname is: {} and your lastname is: {} and your fullname is {}".format(fname, lname, 20))