import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py file.csv")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        rows = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

headers = rows[0]
data = rows[1:]

print(tabulate(data, headers=headers, tablefmt="grid"))
