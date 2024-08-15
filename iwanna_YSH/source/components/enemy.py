import pygame
from .. import  tools,setup
#敌人大类
class Fire(pygame.sprite.Sprite):  #火
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frames=[]
        self.frames_index=0
        frame_rects=[(0,0,35,35),(35,0,35,35),(70,0,35,35)]
        self.load_frames(frame_rects)
        self.image=self.frames[self.frames_index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.timer=0
    #载入火焰素材包
    def load_frames(self,frame_rects):
        sheet=setup.PER['fire']
        for frame_rects in frame_rects:
            self.frames.append(tools.get_image(sheet,*frame_rects,(0,0,0),1))

    def update(self):
        self.current_time=pygame.time.get_ticks()
        frame_durations=[125,125,125]

        if self.timer==0:
            self.timer=self.current_time
        elif self.current_time-self.timer>frame_durations[self.frames_index]:
            self.frames_index+=1
            self.frames_index%=3
            self.timer=self.current_time

        self.image=self.frames[self.frames_index]

class Ghost1(pygame.sprite.Sprite):  #鬼
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frames=[]
        self.frames_index=0
        frame_rects=[(0,0,14,28),(34,0,14,28),(68,0,14,28),(102,0,14,28),(136,0,14,28),(170,0,14,28),(204,0,14,28),(238,0,14,28),(272,0,14,28),(306,0,14,28),(340,0,14,28),(374,0,14,28)]
        self.load_frames(frame_rects)
        self.image=self.frames[self.frames_index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.timer=0

    def load_frames(self,frame_rects):
        sheet=setup.PER['ghost']
        for frame_rects in frame_rects:
            self.frames.append(tools.get_image(sheet,*frame_rects,(0,0,0),1))

    def update(self):
        self.current_time=pygame.time.get_ticks()
        frame_durations=[125,125,125,125,125,125,125,125,125,125,125,125]

        if self.timer==0:
            self.timer=self.current_time
        elif self.current_time-self.timer>frame_durations[self.frames_index]:
            self.frames_index+=1
            self.frames_index%=12
            self.timer=self.current_time

        self.image=self.frames[self.frames_index]

class Ghost2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frames=[]
        self.frames_index=0
        frame_rects=[(0,0,14,28),(34,0,14,28),(68,0,14,28),(102,0,14,28),(136,0,14,28),(170,0,14,28),(204,0,14,28),(238,0,14,28),(272,0,14,28),(306,0,14,28),(340,0,14,28),(374,0,14,28)]
        self.load_frames(frame_rects)
        self.image=self.frames[self.frames_index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.timer=0

    def load_frames(self,frame_rects):
        sheet=setup.PER['ghost2']
        for frame_rects in frame_rects:
            self.frames.append(tools.get_image(sheet,*frame_rects,(0,0,0),1))

    def update(self):
        self.current_time=pygame.time.get_ticks()
        frame_durations=[125,125,125,125,125,125,125,125,125,125,125,125]

        if self.timer==0:
            self.timer=self.current_time
        elif self.current_time-self.timer>frame_durations[self.frames_index]:
            self.frames_index+=1
            self.frames_index%=12
            self.timer=self.current_time

        self.image=self.frames[self.frames_index]