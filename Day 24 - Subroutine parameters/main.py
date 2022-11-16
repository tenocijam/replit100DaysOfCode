# Day 24

import random

print("Infinite Dice 🎲")

def rollDice(sides):
    side = random.randint(1, sides)
    print("You rolled", side)

while True:
    print()
    sides = int(input("How many sides? "))
    rollDice(sides)
    print()
    repeat = input("You want to roll again? ")
    if repeat == "yes":
        continue
    else:
        print()
        print("Thank you!")
        break