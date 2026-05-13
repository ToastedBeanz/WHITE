## ==== WOODS ==== ###
# ::story:: Someone lost in the woods, they have to find stuff to live out there.

import random
import time
import sys
import os
import textwrap
import math
import pygame
from versionhandler import buildTag
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(32)
#import colorama
#from colorama import Fore, Back, Style
import winsound
#colorama.init()
def dialouge(text, speed=1, pap=False, pac=False, pak=False, paa=False): # Range from 0 to 1, 0 being slowest, and 1 being fastest. pap meaning: "pause after period", if true, it will pause for a moment after every period.
    for char in text:
        pygame.mixer.Sound("audio/tck.wav").play()
        sys.stdout.write(char)
        sys.stdout.flush()
        if pap and char == ".":
            time.sleep(0.5)
        elif pac and char == ",":
            time.sleep(0.3)
        elif pak and char == "!":
            time.sleep(0.7)
        elif paa and char == "?":
            time.sleep(0.7)
        time.sleep((1-speed)*0.04) # Adjust the sleep time based on the speed
    #after dialouge is done, clear the terminal text
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal, works for both windows and linux/mac
def animate(animation, text, speed=1):
    if animation == "blink":
        for i in range(3):
            sys.stdout.write(text)
            sys.stdout.flush()
            time.sleep((1-speed)*0.5)
            sys.stdout.write("\r" + " " * len(text) + "\r") # Clear the text
            sys.stdout.flush() # make it all in the same line
            time.sleep((1-speed)*0.5) #control the speed
playerSettings = {
    "vol": 1,
    "sfx": 1,
    "txtspd": 1
}
def printWhite():
    pygame.mixer.music.load("audio/WHITEtitle.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound("audio/tck.wav").play()
    print("""



8b      db      d8
`8b    d88b    d8' 
 `8b  d8'`8b  d8'  
  `8bd8'  `8bd8'   
    YP      YP     
""")
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.mixer.Sound("audio/tck.wav").play()
    print("""
                    88
                    88
                    88
8b      db      d8  88,dPPYba,
`8b    d88b    d8'  88P'    "8a
 `8b  d8'`8b  d8'   88       88
  `8bd8'  `8bd8'    88       88
    YP      YP      88       88""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.mixer.Sound("audio/tck.wav").play()
    print("""
                    88           88                     
                    88           \"\"               
                    88                           
8b      db      d8  88,dPPYba,   88
`8b    d88b    d8'  88P'    "8a  88
 `8b  d8'`8b  d8'   88       88  88 
  `8bd8'  `8bd8'    88       88  88
    YP      YP      88       88  88
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.mixer.Sound("audio/tck.wav").play()
    print("""
                    88           88                     
                    88           \"\"    ,d             
                    88                 88               
8b      db      d8  88,dPPYba,   88  MM88MMM
`8b    d88b    d8'  88P'    "8a  88    88  
 `8b  d8'`8b  d8'   88       88  88    88  
  `8bd8'  `8bd8'    88       88  88    88, 
    YP      YP      88       88  88    "Y888 
""")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.mixer.Sound("audio/tck.wav").play()
    print("""
                    88           88 
                    88           \"\"    ,d               
                    88                 88               
8b      db      d8  88,dPPYba,   88  MM88MMM  ,adPPYba, 
`8b    d88b    d8'  88P'    "8a  88    88    a8P_____88 
 `8b  d8'`8b  d8'   88       88  88    88    8PP\"\"\"\"\"\"\" 
  `8bd8'  `8bd8'    88       88  88    88,   "8b,   ,aa 
    YP      YP      88       88  88    "Y888  `"Ybbd8"' 
                            """ + buildTag() + """
""")

def menu(m):
    while True:
        if m.lower() == "main":
            #winsound.PlaySound("audio/Title.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            printWhite()
            print("Your choices are: ")
            print("1. Start Game")
            print("2. Load Game")
            print("3. Settings")
            print("4. Exit")
            choice = int(input(">: "))
            if choice == 4:
                pygame.mixer.music.stop()
                pygame.mixer.Sound("audio/Transition.mp3").play()
                print("Well you just dont know how to play a game do you?")
                time.sleep(1)
                sys.exit()
            elif choice == 3:
                pygame.mixer.music.stop()
                pygame.mixer.Sound("audio/Transition.mp3").play()
                time.sleep(1)
                pygame.mixer.music.load("audio/Title.mp3")
                pygame.mixer.music.play(-1)
                menu("Settings")
            elif choice == 2:
                print("Sorry, but the load game feature isnt available yet.")
                menu("Main")
            elif choice == 1:
                #get out of the menu loop
                pygame.mixer.music.stop()
                break
                time.sleep(1)


        elif m.lower() == "settings":
            print("Settings: ")
            print("1. Volume")
            print("2. SFX Volume")
            print("3. Text Speed")
            print("4. Sound Test")
            print("5. Back")
            choice = int(input(">: "))
            if choice == 5:
                pygame.mixer.music.stop()
                pygame.mixer.Sound("audio/Transition.mp3").play()
                time.sleep(1)
                pygame.mixer.music.load("audio/Title.mp3")
                pygame.mixer.music.play(-1)
                menu("Main")
            if choice == 1:
                vol = float(input("Volume (0-1): "))
                if vol < 0 or vol > 1:
                    print("Invalid volume.")
                    menu("Settings")
                playerSettings["vol"] = vol
                pygame.mixer.music.set_volume(vol)
                menu("Settings")
            elif choice == 2:
                sfx = float(input("SFX Volume (0-1): "))
                if sfx < 0 or sfx > 1:
                    print("Invalid SFX volume.")
                    menu("Settings")
                playerSettings["sfx"] = sfx
                pygame.mixer.Sound.set_volume(sfx)
                menu("Settings")
            elif choice == 3:
                txtspd = float(input("Text Speed (0-1) (0 is slowest, 1 being fastest): "))
                if txtspd < 0 or txtspd > 1:
                    print("Invalid text speed.")
                    menu("Settings")
                playerSettings["txtspd"] = txtspd
                menu("Settings")
            elif choice == 4:
                print("ehh.. this isnt available yet, but you can test the sounds by going into the audio folder and playing them there.")
                menu("Settings")
                        
                
        elif m.lower() == "sound test":
            print("Sound Test: ")
            sound = input("Enter SOUNDID (tip: SFX starts with an \"S\", and music starts with an \"M\"): ")
            sounds = {
                "S1": "audio/tck.wav",
                "S2": "audio/Transition.mp3",
                "M1": "audio/Title.mp3",
                "M2": "audio/WHITEtitle.mp3"
            }
            if sound in sounds:
                pygame.mixer.Sound(sounds[sound]).play()
            else:
                print("Invalid SOUNDID.")
                menu("Sound Test")
def generateSaveKey(node, item1, item2, item3, item4, item5, HP, maxHP, hunger, maxHunger, thirst, maxThirst):
    n = None # node
    i1 = None # item 1
    i2 = None # item 2
    i3 = None # item 3
    i4 = None # item 4
    i5 = None # item 5
    h = None # HP
    mh = None # max HP
    hu = None # hunger
    mhu = None # max hunger
    t = None # thirst
    mt = None # max thirst

    # turn the values into a set number for each, and include a secutity key, so that people cant just generate a save key by hand
    # == Get back to this later

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)

def main():
    dialouge("You wake up in the middle of the woods, you have no idea how you got there, but you know you have to survive.", 0.1, pap=True, pac=True, pak=True, paa=True)
    dialouge("Welcome... to WHITE.", 0.1, True, True, True, True)
    menu("main")
#breakpoint here to escape any loop, or just use the line `break` */