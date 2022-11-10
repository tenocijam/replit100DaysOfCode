# Day 18

print("Guess the number")
print()

correct_number = 500005
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
