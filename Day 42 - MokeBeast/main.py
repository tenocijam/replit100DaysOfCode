# Day 42

print()
print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

mokedex = {
    "name": None,
    "type": None,
    "special-move": None,
    "hp": None,
    "mp": None
}

for i in mokedex:
     mokedex[i] = input(f"Enter {i}: ").strip().title()

print()

if mokedex["type"] == "Earth":
  print("\033[32m", end="")
elif mokedex["type"] == "Air":
  print("\033[37m", end="")
elif mokedex["type"] == "Fire":
  print("\033[31m", end="")
elif mokedex["type"] =="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for key, value in mokedex.items():
    print(f"{key:<20}:{value}")