# Day 6

print()
print("Secure Login Portal")
print()

username = input("What is your username? ")
passwd = input("What is your password? ")
print()

if username == "John" and passwd == "J123":
    print("Welcome John!")
elif username == "David" and passwd == "qwerty":
    print("Welcome David, have a nice day.")
elif username == "Mat" and passwd == "Matty":
    print("Welcome Mat, hope you are doing good.")
else:
    print("Access denied.")