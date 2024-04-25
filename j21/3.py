import lib


a = "hello world"

lst = []
for i in a:
    lst.append(i)
print(lst)

b = ""

for i in lst:
    b += i
    
print(b)

c = "".join(lst)

print(c)
print(lib.Libclass.sums(5, 6))
print(type(list.append))