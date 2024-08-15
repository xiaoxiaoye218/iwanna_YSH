import pygame
from .. import setup
from .. import tools
from .. components import info
#主菜单
class MainMenu:
    def __init__(self):  #主菜单初始化
        self.setup_background()
        self.setup_cursor()
        self.info=info.Info('main_menu')
        self.finished=False
        self.next='level0'

    def setup_background(self):
        self.background=setup.PER['2']
        self.viewport=setup.SCREEN.get_rect()
    def setup_cursor(self):   #建立光标
        self.cursor=pygame.sprite.Sprite()
        self.cursor.image=tools.get_image(setup.PER['cursor'],0,0,66,66,(0,0,0),1)
        rect=self.cursor.image.get_rect()
        rect.x,rect.y=344,392
        self.cursor.rect=rect
        self.cursor.state='开始游戏'
    #更新光标
    def update_cursor(self,keys):
        if keys[pygame.K_w]:
            self.cursor.state='开始游戏'
            self.cursor.rect.y=392
        elif keys[pygame.K_s]:
            self.cursor.state='退出游戏'
            self.cursor.rect.y=461
        elif keys[pygame.K_RETURN]:
            if self.cursor.state=='开始游戏':
                self.finished=True
            elif self.cursor.state=='退出游戏':
                pygame.display.quit()

    def update(self,surface,keys,n):
        self.n=n

        self.update_cursor(keys)

        surface.blit(self.background,self.viewport)
        surface.blit(self.cursor.image,self.cursor.rect)

        self.info.update()
        self.info.draw(surface)
        return self.n