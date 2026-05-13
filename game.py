import random
import time
import sys
import os
import textwrap
import math
import pygame
from main import playerSettings, animate, main
import nodehandler



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
    clear() # clear the terminal, works for both windows and linux/mac

pygame.init()
pygame.mixer.init()

def clear(what="screen"):
    if what == "screen":
        os.system('cls' if os.name == 'nt' else 'clear')
    if what == "lastline":
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    if what == "lastchar":
        sys.stdout.write("\b \b")

clear("screen")
main()
clear("screen")
