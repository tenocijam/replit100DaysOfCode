# Day 27

import random, os

def roll_dice(sides):
    return random.randint(1, sides)

def generate_character():
    character_name = input("Name your character: ")
    print()
    character_type = input("Enter your character type (Human, Elf, Wizard, Orc): ")
    
    print()
    print("----------------------------")
    print()
    print("Character name:", character_name)
    print("Character type:", character_type)


def generate_character_health():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 10

def generate_character_strength():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 12

while True:
    os.system("clear")
    
    print("Character Generator")
    print()

    generate_character()
    
    print("HEALTH:", int(generate_character_health()))
    print("STRENGTH:", int(generate_character_strength()))

    print()
    repeat = input("Do you want to do again? (yes, no): ")

    if repeat == "yes":   
        continue
    else:
        break