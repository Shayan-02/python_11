list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# Using enumerate to iterate over both lists
for index, (value1, value2) in enumerate(zip(list1, list2)):
    print(f"Index {index}: List1 value: {value1}, List2 value: {value2}")

for index, (value1, value2) in enumerate(zip(list1, list2)):
    print(f"{index} {value2}")
