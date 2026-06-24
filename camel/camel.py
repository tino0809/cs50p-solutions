nombre = input("camelCase: ")

for c in nombre:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")

print()
