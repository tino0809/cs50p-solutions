def main():
    while True:
        fraccion = input("Fraction: ")
        porcentaje = convert(fraccion)
        if porcentaje is not None:
            print(gauge(porcentaje))
            break


def convert(fraccion):
    try:
        x, y = fraccion.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            return None
        if y == 0 or x > y or x < 0:
         return None
        return round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        return None


def gauge(porcentaje):
    if porcentaje <= 1:
        return "E"
    elif porcentaje >= 99:
        return "F"
    else:
        return f"{porcentaje}%"


main()
