with open("test2.txt", "a+") as f:
    # for _ in f:
    #     print(_, end="")
    print(f.read())
    f.write("\nhello world")