x, y, z = input("Expression: ").split()
x = int(x)
z = int(z)

if y == "+":
    resultado = x + z
elif y == "-":
    resultado = x - z
elif y == "*":
    resultado = x * z
elif y == "/":
    resultado = x / z

print(f"{resultado:.1f}")
