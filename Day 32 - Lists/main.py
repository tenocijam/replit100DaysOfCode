# Day 32

import random

print()
print("✨ Tell me your name so that I can greet you")
print()
name = input("What is your name? ")
print()

greetings = ["Bonjour", "Hola", "Guten Tag", "Olá", "Nǐn hǎo", "Goedendag", "Shikamoo"]

while True:
    index = random.randint(0, len(greetings)-1)
    print(f"{greetings[index]}, {name} 👋")
    print()
    repeat = input("Wanna try again? (y/n): ")

    if repeat != "y":
        print()
        print("Thank you!")
        break