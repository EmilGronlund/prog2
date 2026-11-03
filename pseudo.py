import random

slumptal = random.randint(1, 20)

while True:
    gissning = int(input("Gissa ett tal mellan 1 - 20: "))

    if gissning < slumptal:
        print("För lågt!")

    elif gissning > slumptal:
        print("För högt!")

    else:
        print("Rätt!")
        break
