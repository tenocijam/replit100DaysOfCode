# Day 33

import os, time

list = []

def print_list():
    if len(list) != 0:
        for i in list:
            print(i)
    else:
        print("\033[31m⭕ Your list is empty!\033[0m")
    print()
    

def add_to_list(item):
    list.append(item)
    print()
    print("\033[32m✔", item, "was successfully added to your list.\033[0m")
    print()

def remove_from_list(item):
    print()
    if item in list:
        list.remove(item)
        print()
        print("\033[36m✖", item, "was successfully removed from your list.\033[0m")
    else:
        print(f"\033[33m{item} not found in list.\033[0m")
    print()

while True:
    os.system("clear")
    print()
    print("\033[34mTo do list manager\033[0m")
    print()
    print("\033[35mMENU: What do you want to do? \033[0m")
    print("1. View my list")
    print("2. Add item to my list")
    print("3. Remove item from my list")
    print("4. Exit the program")

    print()
    choice = int(input("Enter your choice: "))
    print()
    
    if choice == 1:
        print_list()
        goback = int(input("Type 0 (zero) to go back to menu: "))
        if goback != 0:
            exit()
    elif choice == 2:
        item = input("What do you want to add? ")
        add_to_list(item)
        print("Going back to menu page...")
        time.sleep(2)
    elif choice == 3:
        print("Your list: ")
        print_list()
        item = input("What do you want to remove from the list? ")
        remove_from_list(item)
        print("Going back to menu page...")
        time.sleep(2)
    else:
        print()
        print("Thank you! See you soon...")
        exit()