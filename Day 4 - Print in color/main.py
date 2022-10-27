# Day 4: Print in color
print()
print("\033[34mWelcome to my adventure story generator \033[0m")
print()
print("\033[33mI am going to ask you a bunch of questions and then create an epic story with you as the hero.\033[0m")
print()
print("\033[36m----------------------Created by Sidharth H.----------------------\033[0m")

print()

name = input("What is your name? ")
superpower = input("What is your superpower? ")
enemy_name = input("What is your enemy's name? ")
location = input("Where do you live? ")
food = input("What is your favorite food? ")

print()
print("\033[32mSTORY BEGINS:\033[0m")
print()

print("Hello ", name, ",", sep="")

print("Your ability to", superpower, "will make sure you never have to look at", enemy_name, "again. Go eat", food, "as you walk down the streets of", location, "and use your ability to", superpower, "for good and not evil!")

print()
print("\033[35mThank you!")
print("Hope you liked the story. Have a good day ", name, ".", sep="")