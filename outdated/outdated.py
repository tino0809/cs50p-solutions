meses = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    fecha = input("Date: ").strip()
    try:
        if "/" in fecha:
            mes, dia, anio = fecha.split("/")
            mes = int(mes)
            dia = int(dia)
            anio = int(anio)
        else:
            partes = fecha.split(" ")
            mes_nombre = partes[0]
            if not partes[1].endswith(","):
                continue
            dia = int(partes[1].replace(",", ""))
            anio = int(partes[2])
            if mes_nombre not in meses:
                continue
            mes = meses.index(mes_nombre) + 1

        if mes < 1 or mes > 12 or dia < 1 or dia > 31:
            continue

        print(f"{anio:04}-{mes:02}-{dia:02}")
        break

    except (ValueError, IndexError):
        continue
