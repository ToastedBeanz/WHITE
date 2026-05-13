import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("audio/Title.wav")
pygame.mixer.music.play(-1)

while pygame.mixer.music.get_busy():
    pass