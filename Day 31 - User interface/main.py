# Day 31

def changeColor(color):
  if color=="red":
    return "\033[31m"
  elif color=="green":
    return "\033[32m"
  elif color=="purple":
    return "\033[35m"
  elif color=="cyan":
    return "\033[36m"
  elif color=="yellow":
    return "\033[33m"
  elif color=="blue":
    return "\033[34m"
  else:
    return "\033[0m"


# User interface 1
print("-------------------------------")
print()
print("User interface 1 👇")
print()
title = f"{changeColor('red')}={changeColor('white')}={changeColor('blue')}={changeColor('yellow')} Music App {changeColor('red')}={changeColor('white')}={changeColor('blue')}={changeColor('reset')}"
print(f"{title:^60}")
print()

print("🔥▶ Radio Gaga")
print(f"\t{changeColor('yellow')}Queen{changeColor('reset')}")
print()
print()

prev = "PREV"
next = "NEXT"
pause = "PAUSE"

print(f"{prev}")
print(f"\t\t{changeColor('green')}{next}")
print(f"\t\t\t\t{changeColor('purple')}{pause}{changeColor('reset')}")

# User interface 2
print()
print("-------------------------------")
print()
print("User interface 2 👇")
print()
text = "WELCOME TO"
print(f"{changeColor('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{changeColor('blue')}{text:^35}")
print()
text = "Definitely not a rip off"
print(f"{changeColor('yellow')}{text:>35}")
text = "a certain other social"
print(f"{changeColor('yellow')}{text:>35}")
text = "networking site"
print(f"{changeColor('yellow')}{text:>35}")
print()
text = "Honest."
print(f"{changeColor('red')}{text:^35}")
print()
text = "Username: "
print(f"{changeColor('white')}{text:^35}")
text = "Password: "
print(f"{changeColor('white')}{text:^35}")
print()
print("-------------------------------")