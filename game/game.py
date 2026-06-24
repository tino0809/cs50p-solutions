import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

numero = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
    except ValueError:
        continue

    if guess < numero:
        print("Too small!")
    elif guess > numero:
        print("Too large!")
    else:
        print("Just right!")
        break
