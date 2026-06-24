import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match:
        for i in range(1, 5):
            part = match.group(i)
            if len(part) > 1 and part[0] == "0":
                return False
            if int(part) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
