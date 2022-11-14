# Day 22

import random

print("Guess the number")
print()

correct_number = random.randint(1, 1000000)
attempts = 0

while True:
    print()
    user_number = int(input("Type a number between 0 and 1,000,000 : "))

    if (user_number < 0):
        print("Thank you. Bye!")
        exit()
    elif (user_number < correct_number):
        print("Go high")
        attempts += 1
    elif (user_number > correct_number):
        print("Go low")
        attempts += 1
    else:
        attempts += 1
        print("🎉 You guessed it right!!!")
        print("It took you", attempts, "attempts to guess the correct number.")
        exit()