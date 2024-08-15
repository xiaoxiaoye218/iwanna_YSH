import pygame
from . import constants as C
from . import tools

pygame.init()  #游戏初始化
SCREEN=pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))
pygame.display.set_caption('跃山河')

PER = tools.load_per('resources/per') #素材包