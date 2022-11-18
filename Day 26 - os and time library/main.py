# Day 25

import random

print("⚔ \033[36mCharacter stats generator\033[0m ⚔")
print()

def rollDice(sides):
    side = random.randint(1, sides)
    return side

def health():
    return rollDice(6) * rollDice(8)

while True:
    print()
    character = input("Enter character name: ")
    print(character, "health is", health(), "hp")
    repeat = input("Do you want to continue? (yes/no) ")
    if repeat == "yes":
        continue
    else:
        print()
        print("\033[34mThank you!\033[0m")
        break