# Day 11

print()
total_days = int(input("How many days are there in this year? "))

seconds = total_days * 24 * 60 * 60

if total_days == 366:
    print("There are", seconds, "in this leap year.")
else:
    print("There are", seconds, "in this year.")