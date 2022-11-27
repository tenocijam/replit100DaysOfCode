# Day 35

import os, time

list = []

def print_list():
    count = 0
    if len(list) != 0:
        for i in list:
            print(count, ". ", i, sep="")
            count += 1
    else:
        print("\033[31m⭕ Your list is empty!\033[0m")
    print()
    

def add_to_list(item):
    list.append(item)
    print()
    print("\033[32m✔", item, "was successfully added to your list.\033[0m")
    print()

def remove_from_list(index):
    print()
    if index < len(list):
        answer = input(f"Are you sure you want to remove {list[index]} ? (y/n): ")
        if answer == "y":
            print()
            print("\033[36m✖", list[index], "was successfully removed from your list.\033[0m")
            list.remove(list[index])
    else:
        print("\033[33mInvalid input.\033[0m")
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
    print("4. Clear my list")
    print("5. Exit the program")

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
        index = int(input("Enter the item number you want to remove from the list: "))
        remove_from_list(index)
        print("Going back to menu page...")
        time.sleep(2)
    elif choice == 4:
        list = []
        print("\033[36m✖ Your list has been emptied\033[0m\nGoing back to menu page...")
        time.sleep(2)
    else:
        print()
        print("Thank you! See you soon...")
        exit()