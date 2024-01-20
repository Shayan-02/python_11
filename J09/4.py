lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst[2][1] = 15
print(lst)

t = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
a = list(t)
a[1][0] = "correct"
a[2][2] = "reza"
a[0][1] = "ali"
t = tuple(a)
print(t)
