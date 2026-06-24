texto = input("Input: ")

for c in texto:
    if c.lower() not in "aeiou":
        print(c, end="")

print()
