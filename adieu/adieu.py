import inflect

p = inflect.engine()
nombres = []

while True:
    try:
        nombre = input("Name: ").strip()
        nombres.append(nombre)
    except EOFError:
        break

print(f"\nAdieu, adieu, to {p.join(nombres)}")
