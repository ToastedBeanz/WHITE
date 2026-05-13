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
