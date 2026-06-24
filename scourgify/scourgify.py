import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

try:
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)
        students = list(reader)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        last, first = student["name"].split(", ")
        writer.writerow({"first": first, "last": last, "house": student["house"]})
