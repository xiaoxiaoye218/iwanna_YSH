import pygame
from .. import tools,setup
from .. import constants as C
#主角各个参数
class Player(pygame.sprite.Sprite):   #创建精灵类
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.setup_states()
        self.setup_velocities()
        self.load_images()
        self.can_jump2 = False
        self.can_fall=True
   #玩家初始状态
    def setup_states(self):
        self.state='stand'
        self.face_right=True
   #玩家速度
    def setup_velocities(self):
        self.x_v=0
        self.y_v=0

        self.max_y_v=C.MAX_Y_V
        self.jump_v=C.JUMP_V
        self.g=C.GRAVITY
        self.ag=C.ANTIGRAVITY
   
    def load_images(self):
        sheet=setup.PER['boy']
        self.boy_R=[]
        self.boy_L=[]

        frame_rects=[(0,0,16,35),(17,0,20,37),(38,0,20,34)]

        for frame_rects in frame_rects:
            r_image=tools.get_image(sheet,*frame_rects,(0,0,0),1)
            l_image=pygame.transform.flip(r_image,True,False)
            self.boy_R.append(r_image)
            self.boy_L.append(l_image)

        self.frame_index=0
        self.frames=self.boy_R
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect()
  #玩家各种形态
    def update(self,keys,n,can_fall):
        self.can_fall=can_fall
        self.Can_jump2(n)
        if self.state=='stand':
            self.stand(keys)
        elif self.state=='walk':
            self.walk(keys)
        elif self.state=='jump':
            self.jump(keys)
        elif self.state=='fall':
            self.fall(keys)
        elif self.state=='fall2':
            self.can_fall=self.fall2(keys)
        elif self.state=='jump2':
            self.jump2(keys)


        if self.face_right:
            self.image=self.boy_R[self.frame_index]
        else:
            self.image=self.boy_L[self.frame_index]
        return self.n,self.can_fall
  #二段跳检测
    def Can_jump2(self,n):
        self.n=n
        if self.n>=2:
            self.can_jump2=True
            self.n=0
   #站立函数
    def stand(self,keys):
        self.frame_index=2
        self.x_v=0
        self.y_v=0
        if keys[pygame.K_d]:
            self.face_right=True
            self.state='walk'
        elif keys[pygame.K_a]:
            self.face_right=False
            self.state='walk'
        elif keys[pygame.K_SPACE]:
            self.state='jump'
            self.y_v = self.jump_v

   #行走函数
    def walk(self,keys):
        if keys[pygame.K_d]:
            self.frame_index = 0
            self.face_right=True
            self.x_v=C.x_v
        elif keys[pygame.K_a]:
            self.frame_index = 0
            self.face_right=False
            self.x_v=-C.x_v
        else:
            self.x_v=0
            self.state='stand'
        if keys[pygame.K_SPACE]:
            self.state = 'jump'
            self.y_v = self.jump_v
  #跳跃函数
    def jump(self,keys):
        self.frame_index=0
        self.y_v+=self.ag
        if keys[pygame.K_d]:
            self.face_right=True
            self.x_v=C.x_v
        elif keys[pygame.K_a]:
            self.face_right=False
            self.x_v=-C.x_v
        if keys[pygame.K_SPACE] and self.can_jump2:
            self.y_v=self.jump_v
            self.state='jump2'
        if self.y_v>=0:
            self.state='fall'
  #二段跳函数
    def jump2(self,keys):
        self.can_fall = False
        self.frame_index=1
        self.y_v+=self.ag
        self.can_jump2 = False
        if keys[pygame.K_d]:
            self.face_right=True
            self.x_v=C.x_v
        elif keys[pygame.K_a]:
            self.face_right=False
            self.x_v=-5
        if self.y_v>=0:
            self.state='fall2'
        return self.can_fall
  #下落函数
    def fall(self,keys):
        self.frame_index=2
        self.y_v+=self.g
        if keys[pygame.K_d]:
            self.frame_index = 0
            self.face_right=True
            self.x_v=C.x_v
        elif keys[pygame.K_a]:
            self.frame_index = 0
            self.face_right=False
            self.x_v=-C.x_v
        if keys[pygame.K_SPACE] and self.can_jump2:
            self.y_v=self.jump_v
            self.state='jump2'
#二段下落函数
    def fall2(self,keys):
        self.can_jump2 = False
        self.frame_index = 2
        self.y_v += self.g
        if keys[pygame.K_d]:
            self.frame_index = 0
            self.face_right=True
            self.x_v=C.x_v
        elif keys[pygame.K_a]:
            self.frame_index = 0
            self.face_right=False
            self.x_v=-C.x_v

