def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    sin_signo = d.strip("$")
    return float(sin_signo)


def percent_to_float(p):
    sin_signo = p.strip("%")
    return float(sin_signo) / 100


main()
