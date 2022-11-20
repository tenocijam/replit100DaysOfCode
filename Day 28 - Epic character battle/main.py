# Day 28

import random, os, time

def roll_dice(sides):
    return random.randint(1, sides)

def generate_character_health():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 10

def generate_character_strength():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 12


print("⚔️  BATTLE TIME ⚔️")
print()
time.sleep(1)
    
# Generates character 1
character1_name = input("Name your character: ")
character1_type = input("Enter your character type (Human, Elf, Wizard, Orc): ")

print()
print("----------------------------")
time.sleep(1)
print("😎 Character 1 name:", character1_name)
time.sleep(1)
print("🧬 Character 1 type:", character1_type)
time.sleep(1)
character1_health = int(generate_character_health())
character1_strength = int(generate_character_strength())
print("🩸 Character 1 health:", character1_health)
time.sleep(1)
print("💪 Character 1 strength:", character1_strength)
time.sleep(1)

print()
print("Who are they battling? ")
print()
time.sleep(0.6)

# Generates character 2
character2_name = input("Name your character: ")
character2_type = input("Enter your character type (Human, Elf, Wizard, Orc): ")

print()
print("----------------------------")
time.sleep(1)
print("😎 Character 2 name:", character2_name)
time.sleep(1)
print("🧬 Character 2 type:", character2_type)
time.sleep(1)
character2_health = int(generate_character_health())
character2_strength = int(generate_character_strength())
print("🩸 Character 2 health:", character2_health)
time.sleep(1)
print("💪 Character 2 strength:", character2_strength)
time.sleep(1)

print()
print("⏳ Round 1 loading...")

time.sleep(2.6)

round = 0

while True:
    os.system("clear")
    
    print("⚔️  BATTLE TIME ⚔️")
    time.sleep(1)
    print()

    round += 1
    print("📢 Round", round, "begins!")
    print()
    time.sleep(1.5)

    # Rolls a random 6-sided-dice for both characters
    c1_dice = roll_dice(6)
    c2_dice = roll_dice(6)

    # Checks the damage using the given formula
    damage = abs(character1_strength - character2_strength) + 1

    # Determines the winner and reduces losers health based on the random 6-sided-dice roll
    if c1_dice > c2_dice:
        print("🏆", character1_name, "wins round", round, "and", character2_name, "takes a hit with", damage, "damage.")
        character2_health -= damage
    elif c2_dice > c1_dice:
        print("🏆", character2_name, "wins round", round, "and", character1_name, "takes a hit with", damage, "damage.")
        character1_health -= damage
    else:
        print("🤝 It's a draw between", character1_name, "and", character2_name)


    # Displays health stats of
    print()        
    time.sleep(1.5)
    print("🩸", character1_name, "health:", character1_health)
    time.sleep(1)
    print("🩸", character2_name, "health:", character2_health)
    print()

    time.sleep(1.5)
    # Checks each characters health
    if character1_health <= 0:
        print("💀", character1_name, "has died!")
        print()
        print("🏁 Battle over!!!")
        print()
        print("🥇", character2_name, "has won the battle")
        break
    elif character2_health <= 0:
        print("💀", character2_name, "has died!")
        print()
        print("🏁 Battle over!!!")
        print()
        print("🥇", character1_name, "has won the battle")
        break

    print("⏳ Round", round+1, "loading...")
    time.sleep(2.3)