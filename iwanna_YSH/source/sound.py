import pygame
def music():
   pygame.mixer.init()
   pygame.mixer.music.load('resources/sou/踏山河.mp3')
   pygame.mixer.music.play(-1,0)