# Day 26

from replit import audio
import os, time

def play():
    source = audio.play_file('audio.wav')
    source.paused = False # unpause the playback
    
    user_input = int(input("Press 2 to stop playback and return to menu "))
    
    if user_input == 2:
        source.paused = True
        show_menu()

def show_menu():
    os.system("clear")

    print("🎵 MyPOD Music Player")
    print()
    time.sleep(1)
    print("Press 1 to Play")
    time.sleep(0.5)
    print("Press 2 to Exit")
    time.sleep(0.5)
    print("Press anything else to see the menu again ")
    
    # take user's input
    user_input = int(input())

    if user_input == 1:
        play()
    elif user_input == 2:
        print()
        print("Thank you!")
        exit()
    else:
        show_menu()


show_menu()
