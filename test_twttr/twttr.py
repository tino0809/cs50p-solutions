def main():
    print(shorten(input("Input: ")))


def shorten(word):
    resultado = ""
    for c in word:
        if c.lower() not in "aeiou":
            resultado += c
    return resultado


if __name__ == "__main__":
    main()
