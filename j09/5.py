a = 34895437539845937485
print(len(str(a)))
lst = [1, 2, 3, 4, "a", "b", "a", "a"]
print(lst[5:].count("a"))

a = {1: "a", 2: "b", 3: "c", 4: "d"}
b = {5: "e", 6: "f", 7: "g", 8: "h"}
c = a | b
print(c)