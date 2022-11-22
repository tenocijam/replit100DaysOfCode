# Day 30

print("\033[36mWhat do you feel about the days you have completed in #replit100DaysOfCode\033[36m\n")

for i in range(1,5):
    feedback = input(f"\033[35mDay {i}: \033[0m")
    print()
    message = f"\033[34mYou thought Day {i} was {feedback}. \033[0m"
    print(f"{message: ^65}")
    print()