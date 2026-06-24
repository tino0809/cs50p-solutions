from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    dob = input("Date of Birth: ")
    try:
        birth = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birth, date.today())
    print(f"{p.number_to_words(minutes, andword='').capitalize()} minutes")


def calculate_minutes(birth, today):
    delta = today - birth
    return delta.days * 24 * 60


if __name__ == "__main__":
    main()
