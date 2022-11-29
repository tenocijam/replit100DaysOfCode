# Day 37

print()
print("Star Wars Character Name Generator")
print()

data = input("Enter you first name, lastname, mother's maden name, birth city (in order) seperated by space: ")

data_list = data.split()

if len(data_list) == 4:
    character_name = data_list[0][:3] + data_list[1][:3] + " " + data_list[2][:2] + data_list[3][-3:]

    print()
    print(f"Your Star Wars name is: {character_name.capitalize()}")
else:
    print("Please enter all details properly.")