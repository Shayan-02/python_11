try:
  print(x)
except:
  print("An exception occurred")
finally:
    print("done")


try:
    print("hello")
finally:
    print("done2")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
