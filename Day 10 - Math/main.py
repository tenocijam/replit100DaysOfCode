# Day 10

print()
bill = float(input("What is the total bill? "))

tip = int(input("How much % do you want to tip? "))

totalBill = bill + ((tip / 100) * bill)

people = int(input("How many people are there? "))

owe = totalBill / people

print("You each owe", round(owe, 2))