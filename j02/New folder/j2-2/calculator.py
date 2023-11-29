fn = float(input("first number: "))
sn = float(input("second number: "))

print(fn, "+", sn, "=", fn+sn)
print(fn, "-", sn, "=", fn-sn)
print(fn, "*", sn, "=", fn*sn)
print(fn, "/", sn, "=", fn/sn)

print("------------------------")

print(f"{fn} + {sn} = {fn+sn}")
print(f"{fn} - {sn} = {fn-sn}")
print(f"{fn} * {sn} = {fn*sn}")
print(f"{fn} / {sn} = {fn/sn}")

print("------------------------")

print("{} + {} = {}".format(fn, sn, fn+sn))
print("{} - {} = {}".format(fn, sn, fn-sn))
print("{} * {} = {}".format(fn, sn, fn*sn))
print("{} / {} = {}".format(fn, sn, fn/sn))