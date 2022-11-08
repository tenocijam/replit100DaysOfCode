# Day 16: Name the lyrics game

print()
print("Fill in the blank lyrics!")
print("Type the correct lyrics in the blank space")

attempts = 1

while True:
    print()
    print("🎶 Never going to _______ you up.")
    answer = input("Answer: ")
    
    if answer == "give":
        break
    
    attempts += 1

print()
print("It took you", attempts, "attempts to guess the correct lyrics")