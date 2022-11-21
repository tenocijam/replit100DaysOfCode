# Day 29

def printColor(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="purple":
    print("\033[35m", word, sep="", end="")
  elif color=="cyan":
    print("\033[36m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("My Super Subroutine")
print()
print("With my ", end="")
printColor("red", "new program")
printColor("reset", " I can pass a")
printColor("blue", " color")
printColor("reset", " and a")
printColor("blue", " word")
printColor("reset", " into a")
printColor("purple", " subroutine")
printColor("reset", ", and it will print that")
printColor("green", " word")
printColor("reset", " in that specified")
printColor("green", " color")
printColor("reset", " It's")
printColor("cyan", " cool...")
print()