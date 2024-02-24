import time
import pyttsx3
import emoji
from pyfiglet import Figlet

read_out = pyttsx3.init()

def speak_and_print(message):
    print(message)
    read_out.say(message)
    read_out.runAndWait()

f = Figlet()
ascii_art = f.renderText("Indian Ghost Town")
print(ascii_art)
speak_and_print("Welcome to the Indian Ghost Town " + emoji.emojize(":ghost:") + "...")

def intro():
    speak_and_print(" Hey Brave man, an adventurous soul drawn to mysteries and the supernatural.")
    speak_and_print("Rumors of the abandoned town of Bhangarh, with its centuries-old curses and hauntings, have reached your ears.")
    speak_and_print("You decide to explore the town at night.")
    horror_streets()

def horror_streets():
    speak_and_print("\nChapter 1: The Ghost Town Intro")
    speak_and_print("As you enter the town, deep silence broken by disturbing wind sounds.")
    
    choice = input("1. Continue to the Ghost Town\n2. Get back\nEnter 1 or 2: ")
    if choice == "1":
        ghost_town()
    elif choice == "2":
        speak_and_print("You decided to leave. But the legend of Bhangarh continues to haunt you. Game Over.")
    else:
        speak_and_print("Invalid choice. Please enter 1 or 2.")
        horror_streets()

def ghost_town():
    speak_and_print("\nChapter 1a: In Ghost Town")
    speak_and_print("You encountered by a Dark-Energy.")
    
    choice = input("1. Try chanting some mantras to escape\n2. Hide somewhere\nEnter 1 or 2: ")
    if choice == "1":
        mantra_chant()
    elif choice == "2":
        hide()
    else:
        speak_and_print("Invalid choice. Please enter 1 or 2.")
        ghost_town()

def mantra_chant():
    speak_and_print("\nChapter 1c: The Power of Faith")
    speak_and_print("You start chanting the mantras you learned from your grandmother.")
    time.sleep(2)
    speak_and_print("Unusual things happen around you. The ghost hesitates, then vanishes!")
    time.sleep(1)
    speak_and_print("Journey continues..")
    next_move()

def hide():
    speak_and_print("\nChapter 1b: Ghost Escape")
    time.sleep(1)
    speak_and_print("You found a hidden chamber beneath the temple floor. Inside, there's a Magical Potion and a Note.")
    speak_and_print("Note: 'The potion grants temporary invisibility. Use it wisely.'")
    
    choice = input("1. Sprinkle potion on yourself and escape\n2. Confront the Ghost foolishly\nEnter 1 or 2: ")
    if choice == "1":
        invisibility_escape()
    elif choice == "2":
        speak_and_print("Your bravery is inspiring, but it was not enough. The ghost overpowers you. Game Over.")
    else:
        speak_and_print("Invalid choice. Please enter 1 or 2.")
        hide()

def invisibility_escape():
    speak_and_print("\nChapter 1d: The Invisibility Trick")
    speak_and_print("You sprinkle the potion on yourself and become invisible. The ghost, confused, wanders away.")
    time.sleep(2)
    speak_and_print("You find an ancient scroll hidden in the chamber, revealing the ghost's backstory and how to free the town from the curse.")
    time.sleep(1)
    solve_curse()

def next_move():
    speak_and_print("\nWhat will you do next?")
    
    choice = input("1. Explore the Mysterious haunted Bhangarh_palace\n2. Search for the ancient scroll mentioned in legends\nEnter 1 or 2: ")
    if choice == "1":
        haunted_Bhangarh_palace()
    elif choice == "2":
        ancient_scroll()
    else:
        speak_and_print("Invalid choice. Please enter 1 or 2.")
        next_move()

def haunted_Bhangarh_palace():
    speak_and_print("\nChapter 2: The Haunted_Bhangarh_palace ")
    speak_and_print("Palace filled with huge silence. You feel something around you.")
    speak_and_print("Your Journey continues in Bhangarh_palace")

def ancient_scroll():
    speak_and_print("\nChapter 3: The Quest for the Ancient Scroll")
    speak_and_print("Legends speak of a scroll that contains the secret to lifting the curse on Bhangarh. Your journey leads you towards Ancient Scroll.")
    time.sleep(2)
    speak_and_print("Solved puzzles, riddles, and faced many challenges to find Ancient Scroll.")
    solve_curse()

def solve_curse():
    speak_and_print("\nChapter 4: Lifting the Curse")
    speak_and_print("Learn more about the curse of The Bhangarh and from the knowledge of the Ancient Scroll lifted the curse on the Town.")
    time.sleep(2)
    speak_and_print("Ghost disturbs while you are in the process of removing the curse over The Town.")
    time.sleep(2)
    choice = input("1. Believe in your faith and continue\n2. Quit\nEnter 1 or 2:")
    
    if choice == "1":
        time.sleep(1)
        speak_and_print("Successfully made the Town free from the curse. Game Over!")
    elif choice == "2":
        speak_and_print("You Quit. Game Over.")
    else:
        speak_and_print("Invalid choice. Please enter 1 or 2.")
        solve_curse()

intro()