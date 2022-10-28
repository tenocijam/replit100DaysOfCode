# Day 5: October 28, 2022

print()
print("\033[34mWelcome to Marvel Movie Character Creater\033[0m")
print()
ans1 = input("Do you like hanging around? (Y/N) : ")

if ans1 == "Y":
    print("\033[35mYou must be Spider-man!\033[0m")
    print()

ans2 = input("Do you have a gravelly voice? (Y/N) : ")
    
if ans2 == "Y":
    print("\033[35mThen you must be Korg\033[0m")
    print()

ans3 = input("Do you often feel Marvelous? (Y/N) : ")

if ans3 == "Y":
    print("\033[35mYup! you are Captain Marvel!\033[0m")
    print()
        
if ans1 == "N" and ans2 == "N" and ans3 == "N":
    print()
    print("\033[36mI think you are not like any of the Marvel characters :(\033[0m")

