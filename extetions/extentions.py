nombre = input("File name: ").strip().lower()

if nombre.endswith(".gif"):
    print("image/gif")
elif nombre.endswith(".jpg") or nombre.endswith(".jpeg"):
    print("image/jpeg")
elif nombre.endswith(".png"):
    print("image/png")
elif nombre.endswith(".pdf"):
    print("application/pdf")
elif nombre.endswith(".txt"):
    print("text/plain")
elif nombre.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
