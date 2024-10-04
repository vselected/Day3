
if __name__ == '__main__':
    print('PyCharm')

    #Print formatting with Strings
    print("This is a string {}".format("Inserted"))
    print("The {2} {1} {0}".format("fox", "brown", "quick"))
    print("The {q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))

    #Print formating with float
    result = 0.4231421432
    print("The result was {}".format(result))
    print("The result was {r}".format(r = result))

    #Float formatting "{value:width.precision f}"
    print("The result was {r:1.5f}".format(r=result))

    name = "John"
    age = 3
    print(f"My name is {name} and I have {age} years")


