# Day 40

print()
print("Contact form")
print()

name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")

contact = {
    "name": name,
    "dob": dob,
    "tel": tel,
    "email": email,
    "address": address
}

print()
print("-----------------------------------------")
print()

print(f"Your name is {contact['name']}. You was born on {contact['dob']}. We can ping you on {contact['tel']}, or email you on {contact['email']} or send a post to {contact['address']}.")