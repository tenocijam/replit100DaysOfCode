# Day 23

print("🔐 Welcome to Replit Login System")

def login():
    print()
    username = input("What is your username? ")
    password = input("What is your password? ")
    print()

    if username != "john" or password != "pass123":
        print("\033[31mIncorrect credentials\033[0m")
        login()


login()
print("\033[32mWelcome to Replit!\033[0m")