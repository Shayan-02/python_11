# function that filters vowels
def fun(variable):
    letters = ["a", "e", "i", "o", "u"]
    if variable in letters:
        return variable



# sequence
sequence = ["g", "e", "e", "j", "k", "s", "p", "r"]

# using filter function
# filtered = filter(fun, sequence)

# print("The filtered letters are:")
for i in sequence:
    print(fun(i))
