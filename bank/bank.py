saludo = input("Greeting: ").strip().lower()

if saludo.startswith("hello"):
    print("$0")
elif saludo.startswith("h"):
    print("$20")
else:
    print("$100")
