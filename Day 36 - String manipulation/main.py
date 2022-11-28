# Day 36

print()
print("Name list")

list = []

while True:
    print()
    fname = input("Enter first name: ").strip().capitalize()
    lname = input("Enter last name: ").strip().capitalize()

    full_name = f"{fname} {lname}"

    if full_name not in list:
        list.append(full_name)
        print(f"{full_name} was added successfully to the list.")
    else:
        print("Entry ignored. Reason: duplicate.")

    print()
    print("Your name list: ")
    for name in list:
        print(name)
    print()
    print("-----------------------")