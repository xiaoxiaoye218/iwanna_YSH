import pygame
import os
from . import sound
class Game:  #游戏主体
    def __init__(self,state_dict,start_state):
        self.screen=pygame.display.get_surface()
        self.clock=pygame.time.Clock()
        self.keys=pygame.key.get_pressed()
        self.state_dict=state_dict
        self.state=self.state_dict[start_state]
        self.n=0

    def update(self):
        if self.state.finished:
            next_state=self.state.next
            self.state.finished=False
            self.state=self.state_dict[next_state]
        self.n=self.state.update(self.screen,self.keys,self.n)
        return self.n
    #运行游戏
    def run(self):
        sound.music()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.display.quit()
                elif event.type==pygame.KEYDOWN:   #检测是否按下键盘
                    self.keys=pygame.key.get_pressed()
                    if self.keys[pygame.K_SPACE]:
                        self.n+=1
                    if self.keys[pygame.K_ESCAPE]:
                        pygame.display.quit()
                elif event.type==pygame.KEYUP:   #检测是否按下键盘
                    self.keys=pygame.key.get_pressed()


            self.n=self.update()


            pygame.display.update()
            self.clock.tick(60)
#载入素材包
def load_per(path,accept=('.jpg','.png','.bmp','.gif')): #载入素材库
    per={}
    for pic in os.listdir(path):
        name,ext=os.path.splitext(pic)  #分离文件名与后缀
        if ext.lower()in accept:  #判断是否为可接受格式
            img=pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img=img.convert_alpha()
            else:
                img=img.convert()
            per[name]=img
    return per
def get_image(sheet,x,y,width,height,colorkey,scale):   #sheet是导入的图像，x，y是所需部分在图片中位置的左上像素点的坐标,width,heigh是宽高，colorkey是要扣掉的背景色，scale是放大倍数
    image=pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(colorkey)
    image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image
