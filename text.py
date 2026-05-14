import pygame
import sys
import time
import os
class Text:
    def __init__(self, text):
        self.__text = text

    def dialog(self, speed=1, clearTerminal=False, pap=False, pac=False, pak=False, paa=False): # Range from 0 to 1, 0 being slowest, and 1 being fastest. pap meaning: "pause after period", if true, it will pause for a moment after every period.
        text = self.__text
        for char in text:
            pygame.mixer.Sound("audio/tck.mp3").play()
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
            time.sleep((1-speed)*0.04) #speed of typing
        time.sleep(1)
        if clearTerminal:
            os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal, works for both windows and linux/mac
    def clear(what="screen"):
        if what == "screen":
            os.system('cls' if os.name == 'nt' else 'clear')
        if what == "lastline":
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        if what == "lastchar":
            sys.stdout.write("\b \b")
    def test():
        print("testing text.")
        time.sleep(1)
        print(".", flush=True)
        time.sleep(1)
        print(".", flush=True)
        time.sleep(1)
        print("Test 1: ASCII") 
        ASCII_CHARS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        for char in ASCII_CHARS:
            sys.stdout.write(f"\"{char}\"")

"""

=== Commands ===
Text.dialouge(text="Text Here", speed=0.1, clearTerminal=False, pap=False, pac=False, pak=False, paa=False)
Text.test()

"""