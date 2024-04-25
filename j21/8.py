keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
p_dict = {keys[i]: values[i] for i in range(len(keys))}
print(p_dict)  # Prints {'name': 'Alice', 'age': 30, 'city': 'New York'}


person_dict = dict(zip(keys, values))
print(person_dict)  # Prints {'name': 'Alice', 'age': 30, 'city': 'New York'}