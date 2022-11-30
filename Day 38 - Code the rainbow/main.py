# Day 38

print()
sentence = input("What sentense do you want to rainbow-ize? ")

def changeColor(color):
  if color=="red":
    print("\033[31m", end="")
  elif color=="green":
    print("\033[32m", end="")
  elif color=="purple":
    print("\033[35m", end="")
  elif color=="yellow":
    print("\033[33m", end="")
  elif color=="blue":
    print("\033[34m", end="")
  else:
    print("\033[0m", end="")

print()      

for letter in sentence:
    if letter.lower() == "r":
        changeColor("red")
    elif letter.lower() == "b":
        changeColor("blue")
    elif letter.lower() == "g":
        changeColor("green")
    elif letter.lower() == "p":
        changeColor("purple")
    elif letter.lower() == "y":
        changeColor("yellow")
    elif letter.isspace():
        changeColor("white")
    print(letter, end="")

print()