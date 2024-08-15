import pygame

pygame.font.init()


#文字信息载入
class Info:
    def __init__(self,state):
        self.state=state
        self.create_state_labels()

    def create_state_labels(self):
        self.state_labels=[]
        if self.state=='main_menu':
            self.state_labels.append((self.create_label('开始游戏'),(400,400)))
            self.state_labels.append((self.create_label('退出游戏'), (400, 466)))
            self.state_labels.append((self.create_label('按回车开始'), (380, 600)))
            self.state_labels.append((self.create_label('跃山河',125), (100, 125)))
        elif self.state=='level0':
            self.state_labels.append((self.create_label('按“A”左移，按“D”右移，按“空格”跳跃',color=(33,85,81)),(0,0)))
            self.state_labels.append((self.create_label('若无法移动，请把输入法调整至英文',size=20,color=(33,85,81)),(0,50)))
        elif self.state=='level1':
            pass
        elif self.state=='level2':
            pass
        elif self.state=='level3':
            pass
        elif self.state=='level4':
            self.state_labels.append((self.create_label('不朽荣光！',size=110,color=(237,172,59)),(380,50)))
            self.state_labels.append((self.create_label('按ESC退出',20),(0,0)))


    def create_label(self,label,size=40,width_scale=1.25,height_scale=1,color=(255,255,255)):
        font=pygame.font.Font('resources/fonts/1.ttf',size)
        label_image=font.render(label,1,color)
        return label_image

    def update(self):
        pass

    def draw(self,surface):
        for label in self.state_labels:
            surface.blit(label[0],label[1])