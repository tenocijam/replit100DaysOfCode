# Day 15

exit = "no"

while exit != "yes":
    print()
    
    animal = input("What animal sound do you want to know? ")
    if animal == "cow":
        print("Moo 🐄")
    elif animal == "cat":
        print("Meow 🐈")
    elif animal == "dog":
        print("Bow bow 🐶")
    elif animal == "duck":
        print("Quack quack 🦆")
    else:
        print("I don't know that animal sound. Please try some other animal.")
    
    exit = input("Do you want to exit? ")

print()
print("Thank you! See you soon...")