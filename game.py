import random
import time
import sys
import os
import textwrap
import math
import pygame
from main import playerSettings, animate, main
from nodehandler import Nodehandler
from player import Player
from text import Text
# from passwordhandler import 
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
def startup():
    my_text = Text("Hello, world!")
    my_text.dialog()
    pygame.mixer.Sound("audio/start.mp3").play()
    print("""==== credits:
    Plot designer: ToastedBeanz   
    Main Programmer: Noah Keyes
    Debugger: ToastedBeanz""")
    time.sleep(5.5719)
    clear("screen")
    time.sleep(5.5719)
    main()
    clear("screen")

startup()

