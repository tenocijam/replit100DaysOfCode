# Day 7

print ("True fan detector")
print()
print("Answer these questions to find out whether you are a true fan of 'Stranger Things'")
print()

seasons = input("How many seasons of 'Stranger Things' have been released? ")
print()

if seasons == "4":
    print("Correct!")
    print()

    actress = input("Who is the well-known actress who plays Will Byers mother? ")
    print()
    if actress == "winona ryder":
        print("You are right!")
        print("You are a true fan of 'Stranger Things' 🎉")
    else:
        print("Wrong answer")
else:
    print("Wrong!")
    print("You are a FAKE fan 😡")