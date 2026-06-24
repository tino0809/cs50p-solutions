lista = {}

while True:
    try:
        item = input().strip().upper()
        if item in lista:
            lista[item] += 1
        else:
            lista[item] = 1
    except EOFError:
        break

for item in sorted(lista):
    print(lista[item], item)
