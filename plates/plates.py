def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   
    if len(s) < 2 or len(s) > 6:
        return False


    if not s.isalnum():
        return False


    if not s[0].isalpha() or not s[1].isalpha():
        return False


    numero_iniciado = False
    for c in s:
        if c.isdigit():
            if not numero_iniciado and c == "0":
                return False
            numero_iniciado = True
        else:
            if numero_iniciado:
                return False

    return True


main()
