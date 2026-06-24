import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input output")

input_file = sys.argv[1].lower()
output_file = sys.argv[2].lower()

valid_extensions = [".jpg", ".jpeg", ".png"]

if not any(input_file.endswith(ext) for ext in valid_extensions):
    sys.exit("Invalid input extension")

if not any(output_file.endswith(ext) for ext in valid_extensions):
    sys.exit("Invalid output extension")

input_ext = "." + input_file.split(".")[-1]
output_ext = "." + output_file.split(".")[-1]

if input_ext != output_ext:
    sys.exit("Input and output must have the same extension")

try:
    photo = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input file does not exist")

shirt = Image.open("shirt.png")

photo = ImageOps.fit(photo, shirt.size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
