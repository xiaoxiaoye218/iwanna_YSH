import pygame
from .. components import info
from .. import setup
from ..components import player,stuff,enemy
from .. import constants as C
#场景代码
class level0:   
    def __init__(self):
        self.finished=False
        self.next='level3'
        self.info=info.Info('level0') 
        self.setup_background()
        self.setup_player()
        self.setup_ground_items()
        self.can_fall=True
        self.setup_enemy()

    def setup_background(self):
        self.background=setup.PER['k1.1']    
    #创立玩家及初始位置
    def setup_player(self):
        self.player=player.Player('boy')
        self.player.rect.x=C.x_0
        self.player.rect.y=C.y_0

    def setup_ground_items(self):
        self.brick=[(0,665,1200,35),(0,530,945,35),(0,0,5,700),(1199,0,1,700)]  #导入砖块位置
        self.ground_item_group=pygame.sprite.Group()
        for location in self.brick:
            self.ground_item_group.add(stuff.Item(*location))    #对brick中元素进行解码
        self.end=[(0,350,35,35)]                           
        self.ending = pygame.sprite.Group()
        for location in self.end:
            self.ending.add(stuff.Item(*location))

    def setup_enemy(self):
        self.fire=[(350,630)]                          #加入障碍物坐标
        self.enemy_group=pygame.sprite.Group()
        for locations in self.fire:
            self.enemy_group.add(enemy.Fire(*locations))
        self.ghost1=[(350,455)]                        #加入障碍物坐标
        for locations in self.ghost1:
            self.enemy_group.add(enemy.Ghost1(*locations))
        self.ghost2=[]                                 #加入障碍物坐标
        for locations in self.ghost2:
            self.enemy_group.add(enemy.Ghost2(*locations))
   #刷新画面
    def update(self,surface,keys,n):
        self.check_end()
        self.check_die()
        self.enemy_group.update()
        self.n=n
        self.n,self.can_fall=self.player.update(keys,self.n,self.can_fall)
        self.n,self.can_fall=self.update_player_position(self.n,self.can_fall)
        self.draw(surface)
        return self.n
  #刷新人物位置
    def update_player_position(self,n,can_fall):
        self.can_fall=can_fall
        self.n = n
        self.player.rect.x+=self.player.x_v
        self.check_x_collisions()
        self.player.rect.y+=self.player.y_v
        self.n,self.can_fall=self.check_y_collisions(self.n,self.can_fall)
        self.check_will_fall(self.player, self.can_fall)
        return self.n,self.can_fall
  #检查水平方向碰撞
    def check_x_collisions(self):
        grond_item=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if grond_item:
            self.adjust_player_x(grond_item)
  #竖直方向碰撞
    def check_y_collisions(self,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        grond_item = pygame.sprite.spritecollideany(self.player, self.ground_item_group)
        if grond_item:
            self.n,self.can_fall=self.adjust_player_y(grond_item,self.n,self.can_fall)
        return self.n,self.can_fall
  #碰撞后调整人物方向位置
    def adjust_player_x(self,sprite):
        if self.player.rect.x<sprite.rect.x:
            self.player.rect.right=sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_v=0
  #竖直位置
    def adjust_player_y(self,sprite,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        if self.player.rect.bottom<sprite.rect.bottom:
            self.player.y_v=0
            self.player.rect.bottom=sprite.rect.top
            self.n=0
            self.player.state='walk'
            self.can_fall = True
        else:
            self.player.y_v=1
            self.player.rect.top=sprite.rect.bottom
            if self.can_fall:
                self.player.state='fall'
            else:
                self.player.state='fall2'
        return self.n,self.can_fall
   #检测是否下落
    def check_will_fall(self,sprite,can_fall):
        self.can_fall=can_fall
        sprite.rect.y+=1
        collided=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if not collided and sprite.state!='jump' and sprite.state!='jump2':
            if self.can_fall:
                sprite.state='fall'
            else:
                sprite.state = 'fall2'
        sprite.rect.y-=1
  #跟新图片窗口
    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.player.image,self.player.rect)
        self.info.draw(surface)
        self.enemy_group.draw(surface)
  #检测死亡
    def check_die(self):
        collided = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if collided:
            self.player.rect.x=C.x_0
            self.player.rect.y=C.y_0
            self.player.state='walk'
  #检测到达终点
    def check_end(self):
        collided = pygame.sprite.spritecollideany(self.player, self.ending)
        if collided:
            self.finished = True
#关卡3
class level1:
    def __init__(self):
        self.finished=False
        self.next='level4'
        self.info=info.Info('level1')
        self.setup_background()
        self.setup_player()
        self.setup_ground_items()
        self.can_fall=True
        self.setup_enemy()

    def setup_background(self):
        self.background=setup.PER['k2']     #将引用的背景图名字写入

    def setup_player(self):
        self.player=player.Player('boy')
        self.player.rect.x=C.x_1      #人物初始位置横坐标，需要在constants.py文件里改变x_1的值
        self.player.rect.y=C.y_1      #人物初始位置横坐标，需要在改y_1

    def setup_ground_items(self):
        self.brick=[(0,665,1200,35),(0,0,5,700),(1199,0,1,700),(0,508,128,35),(193,543,35,35),
        (228,149,35,600),(93,630,35,35),(46,394,35,35),(0,287,35,35),(228,114,735,35),
        (129,202,35,35),(406,79,35,35),(578,79,35,35),(750,79,35,35),(360,270,1000,35),(715,149,35,35),
        (715,235,35,35),(820,235,35,35),(360,235,35,35),(817,149,35,15),(263,436,805,35),(441,305,35,35),(578,305,35,35),
        (509,400,35,35),(648,400,35,35),(715,305,35,35),(770,470,7*35,35),(840,505,35,70,),(910,505,35,70),(733,565,35,105),
        (768,600,35,70),(803,635,35,35),(946,630,35,35),(981,595,35,70),(1016,560,35,105),(298,561,35,105),(406,579,35,35),
        (509,579,35,35),(613,579,35,35)]      #先在ps里面把砖块添加，例如k1.1，再到此处填入坐标（左上角x值，左上角y值，宽度，长度）
        self.ground_item_group=pygame.sprite.Group()
        for location in self.brick:
            self.ground_item_group.add(stuff.Item(*location))
        self.end=[(263,630,35,35)]                               #设置终点位置，在ps上加入终点图像
        self.ending = pygame.sprite.Group()
        for location in self.end:
            self.ending.add(stuff.Item(*location))

    def setup_enemy(self):
        self.fire=[(58,630),(93,473),(406,44),(578,44),(750,44),(441,79),(613,79),(785,79),(370,79),(543,79),(715,79),
        (1070,235),(1035,235),(750,235),(785,235),(395,235),(263,400),(298,400),(333,400),(880,400),(1050,627),(1165,627),
        (698,630),(663,630),(628,630),(593,630),(558,630),(523,630),(488,630),(453,630),(418,630),(383,630),(348,630),
        ]                    #加入障碍物坐标，只需在中括号后加坐标，自动出现图像，其他无需改变
        self.enemy_group=pygame.sprite.Group()
        for locations in self.fire:
            self.enemy_group.add(enemy.Fire(*locations))
        self.ghost1=[(578,235),(578,205),(263,288),(263,328),(822,506),(946,504)]    #右朝向鬼
        for locations in self.ghost1:
            self.enemy_group.add(enemy.Ghost1(*locations))
        self.ghost2=[(110,202),(970,114),(1000,114),(1120,114),(1150,114),(441,340),(578,340),(510,309),
        (657,305),(720,340),(880,304),(1068,434),(1180,510)]                        #左朝向鬼
        for locations in self.ghost2:
            self.enemy_group.add(enemy.Ghost2(*locations))

    def update(self,surface,keys,n):
        self.check_end()
        self.check_die()
        self.enemy_group.update()
        self.n=n
        self.n,self.can_fall=self.player.update(keys,self.n,self.can_fall)
        self.n,self.can_fall=self.update_player_position(self.n,self.can_fall)
        self.draw(surface)
        return self.n

    def update_player_position(self,n,can_fall):
        self.can_fall=can_fall
        self.n = n
        self.player.rect.x+=self.player.x_v
        self.check_x_collisions()
        self.player.rect.y+=self.player.y_v
        self.n,self.can_fall=self.check_y_collisions(self.n,self.can_fall)
        return self.n,self.can_fall

    def check_x_collisions(self):
        grond_item=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if grond_item:
            self.adjust_player_x(grond_item)

    def check_y_collisions(self,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        grond_item = pygame.sprite.spritecollideany(self.player, self.ground_item_group)
        if grond_item:
            self.n,self.can_fall=self.adjust_player_y(grond_item,self.n,self.can_fall)
        self.check_will_fall(self.player)
        return self.n,self.can_fall

    def adjust_player_x(self,sprite):
        if self.player.rect.x<sprite.rect.x:
            self.player.rect.right=sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_v=0

    def adjust_player_y(self,sprite,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        if self.player.rect.bottom<sprite.rect.bottom:
            self.player.y_v=0
            self.player.rect.bottom=sprite.rect.top
            self.n=0
            self.player.state='walk'
            self.can_fall = True
        else:
            self.player.y_v=C.r_v
            self.player.rect.top=sprite.rect.bottom
            if self.can_fall:
                self.player.state='fall'
            else:
                self.player.state='fall2'
        return self.n,self.can_fall

    def check_will_fall(self,sprite):
        sprite.rect.y+=1
        collided=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if not collided and sprite.state!='jump' and sprite.state!='jump2':
            if self.can_fall:
                sprite.state='fall'
            else:
                sprite.state='fall2'
        sprite.rect.y-=1

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.player.image,self.player.rect)
        self.info.draw(surface)
        self.enemy_group.draw(surface)

    def check_die(self):
        collided = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if collided:
            self.player.rect.x=C.x_1
            self.player.rect.y=C.y_1
            self.player.state='walk'

    def check_end(self):
        collided = pygame.sprite.spritecollideany(self.player, self.ending)
        if collided:
            self.finished = True
#关卡2
class level2:
    def __init__(self):
        self.finished=False
        self.next='level1'
        self.info=info.Info('level2')
        self.setup_background()
        self.setup_player()
        self.setup_ground_items()
        self.can_fall=True
        self.setup_enemy()

    def setup_background(self):
        self.background=setup.PER['k3']     #将引用的背景图名字写入

    def setup_player(self):
        self.player=player.Player('boy')
        self.player.rect.x=C.x_2      #人物初始位置横坐标，需要在constants.py文件里改变x_1的值
        self.player.rect.y=C.y_2      #人物初始位置横坐标，需要在改y_1

    def setup_ground_items(self):
        self.brick=[(35,91,155,35),(0,0,36,700),(0,665,1200,35),(0,0,1200,18),(360,18,355,35),
                    (403,55,270,35),(438,85,193,35),(155,170,35,170),(188,203,141,64),
                    (330,232,89,35),(551,231,90,35),(713,232,35,35),(782,199,35,70),(850,128,35,35),
                    (850,166,175,35),(1057,166,35,35),(1165,18,35,650),(120,567,35,100),
                    (119,473,35,35),(153,439,35,35),(188,406,35,35),(223,370,70,35),(293,406,35,35),
                    (329,440,70,35),(396,475,35,70),(430,511,35,35),(467,477,35,105),
                    (501,546,214,35),(188,521,140,35),(502,441,70,35),(572,406,35,35),
                    (606,370,70,35),(677,406,35,35),(712,441,35,35),(748,476,35,35),(746,631,35,35),
                    (818,545,35,35),(853,580,35,35),(888,615,35,35),(850,441,35,35),(903,507,35,35),
                    (292,270,492,35)]      #先在ps里面把砖块添加，例如k1.1，再到此处填入坐标（左上角x值，左上角y值，宽度，长度）
        self.ground_item_group=pygame.sprite.Group()
        for location in self.brick:
            self.ground_item_group.add(stuff.Item(*location))
        self.end=[(573,441,35,35)]                               #设置终点位置，在ps上加入终点图像
        self.ending = pygame.sprite.Group()
        for location in self.end:
            self.ending.add(stuff.Item(*location))

    def setup_enemy(self):
        self.fire=[(197,92),(329,595),(189,168),(241,168),(291,168),
                   (416,233),(464,233),(512,233),(639,231),(678,231),
                   (748,231),(816,166),
                   (1022,166),(998,630),(327,406),(431,477),
                   (294,630),(364,630),(501,409),(570,371),(998,630)]                    #加入障碍物坐标，只需在中括号后加坐标，自动出现图像，其他无需改变
        self.enemy_group=pygame.sprite.Group()
        for locations in self.fire:
            self.enemy_group.add(enemy.Fire(*locations))
        self.ghost1=[(189,304),(258,406),(576,475),(783,511),(714,19),(800,18),(946,18),(1055,18)]    #同fire
        for locations in self.ghost1:
            self.enemy_group.add(enemy.Ghost1(*locations))
        self.ghost2=[(119,169),(223,406),(1088,238),(1130,458)]                        #左朝向鬼
        for locations in self.ghost2:
            self.enemy_group.add(enemy.Ghost2(*locations))

    def update(self,surface,keys,n):
        self.check_end()
        self.check_die()
        self.enemy_group.update()
        self.n=n
        self.n,self.can_fall=self.player.update(keys,self.n,self.can_fall)
        self.n,self.can_fall=self.update_player_position(self.n,self.can_fall)
        self.draw(surface)
        return self.n

    def update_player_position(self,n,can_fall):
        self.can_fall=can_fall
        self.n = n
        self.player.rect.x+=self.player.x_v
        self.check_x_collisions()
        self.player.rect.y+=self.player.y_v
        self.n,self.can_fall=self.check_y_collisions(self.n,self.can_fall)
        return self.n,self.can_fall

    def check_x_collisions(self):
        grond_item=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if grond_item:
            self.adjust_player_x(grond_item)

    def check_y_collisions(self,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        grond_item = pygame.sprite.spritecollideany(self.player, self.ground_item_group)
        if grond_item:
            self.n,self.can_fall=self.adjust_player_y(grond_item,self.n,self.can_fall)
        self.check_will_fall(self.player)
        return self.n,self.can_fall

    def adjust_player_x(self,sprite):
        if self.player.rect.x<sprite.rect.x:
            self.player.rect.right=sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_v=0

    def adjust_player_y(self,sprite,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        if self.player.rect.bottom<sprite.rect.bottom:
            self.player.y_v=0
            self.player.rect.bottom=sprite.rect.top
            self.n=0
            self.player.state='walk'
            self.can_fall=True
        else:
            self.player.y_v=C.r_v
            self.player.rect.top=sprite.rect.bottom
            if self.can_fall:
                self.player.state='fall'
            else:
                self.player.state='fall2'
        return self.n,self.can_fall

    def check_will_fall(self,sprite):
        sprite.rect.y+=1
        collided=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if not collided and sprite.state!='jump' and sprite.state!='jump2':
            if self.can_fall:
                sprite.state='fall'
            else:
                sprite.state = 'fall2'
        sprite.rect.y-=1

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.player.image,self.player.rect)
        self.info.draw(surface)
        self.enemy_group.draw(surface)

    def check_die(self):
        collided = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if collided:
            self.player.rect.x=C.x_2
            self.player.rect.y=C.y_2
            self.player.state='walk'

    def check_end(self):
        collided = pygame.sprite.spritecollideany(self.player, self.ending)
        if collided:
            self.finished = True
#关卡1
class level3:
    def __init__(self):
        self.finished=False
        self.next='level2'
        self.info=info.Info('level3')
        self.setup_background()
        self.setup_player()
        self.setup_ground_items()
        self.can_fall=True
        self.setup_enemy()

    def setup_background(self):
        self.background=setup.PER['k4']     #将引用的背景图名字写入

    def setup_player(self):
        self.player=player.Player('boy')
        self.player.rect.x=C.x_3
             #人物初始位置横坐标，需要在constants.py文件里改变x_1的值
        self.player.rect.y=C.y_3      #人物初始位置横坐标，需要在改y_1

    def setup_ground_items(self):
        self.brick=[(0,665,1200,35),(0,0,35,700),(35,0,175,35),(35,228,70,35),(35,473,70,35),(105,263,70,3),
        (175,298,35,35),(140,404,140,35),(280,89,270,35),(245,124,140,35),(175,159,210,35),(350,193,35,61),
        (350,254,227,35),(420,420,312,35),(420,456,35,210),(772,421,70,35),(804,456,35,105),
        (804,596,35,70),(824,71,70,35),(824,176,140,35),(1024,0,168,33),(1165,33,35,388),(942,264,100,35),(1021,176,140,35),(1924,281,125,35),(1095,267,70,35),
        (867,343,246,35),(1082,421,118,35),(1047,456,153,35),(1019,491,181,35),(982,526,67,35),(940,561,75,35),(895,596,137,35),
        (875,631,322,35),(1152,526,48,105),(0,665,1200,35),(622,561,70,103),(140,543,176,35),(787,0,37,289),(649,253,175,35),(455,559,70,107),
        (521,631,100,35)]      #先在p里面把砖块添加，例如k1.1，再到此处填入坐标（左上角x值，左上角y值，宽度，长度）
        self.ground_item_group=pygame.sprite.Group()
        for location in self.brick:
            self.ground_item_group.add(stuff.Item(*location))
        self.end=[(824,34,36,36)]                               #设置终点位置，在ps上加入终点图像
        self.ending = pygame.sprite.Group()
        for location in self.end:
            self.ending.add(stuff.Item(*location))

    def setup_enemy(self):
        self.fire=[(35,196),(210,508),(245,508),(200,631),(342,54),(399,54),(579,386),(614,386),(894,142),(947,314)]                    #%%%%%%%%加入障碍物坐标，只需在中括号后加坐标，自动出现图像，其他无需改变
        self.enemy_group=pygame.sprite.Group()
        for locations in self.fire:
            self.enemy_group.add(enemy.Fire(*locations))
        self.ghost1=[(210,0),(245,0),(558,214)]    #同fire
        for locations in self.ghost1:
            self.enemy_group.add(enemy.Ghost1(*locations))
        self.ghost2=[(648,51),(648,86),(839,349),(861,524),(386,421),(386,456)]                        #左朝向鬼
        for locations in self.ghost2:
            self.enemy_group.add(enemy.Ghost2(*locations))

    def update(self,surface,keys,n):
        self.check_end()
        self.check_die()
        self.enemy_group.update()
        self.n=n
        self.n,self.can_fall=self.player.update(keys,self.n,self.can_fall)
        self.n,self.can_fall=self.update_player_position(self.n,self.can_fall)
        self.draw(surface)
        return self.n

    def update_player_position(self,n,can_fall):
        self.can_fall=can_fall
        self.n = n
        self.player.rect.x+=self.player.x_v
        self.check_x_collisions()
        self.player.rect.y+=self.player.y_v
        self.n,self.can_fall=self.check_y_collisions(self.n,self.can_fall)
        return self.n,self.can_fall

    def check_x_collisions(self):
        grond_item=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if grond_item:
            self.adjust_player_x(grond_item)

    def check_y_collisions(self,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        grond_item = pygame.sprite.spritecollideany(self.player, self.ground_item_group)
        if grond_item:
            self.n,self.can_fall=self.adjust_player_y(grond_item,self.n,self.can_fall)
        self.check_will_fall(self.player)
        return self.n,self.can_fall

    def adjust_player_x(self,sprite):
        if self.player.rect.x<sprite.rect.x:
            self.player.rect.right=sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_v=0

    def adjust_player_y(self,sprite,n,can_fall):
        self.can_fall=can_fall
        self.n=n
        if self.player.rect.bottom<sprite.rect.bottom:
            self.player.y_v=0
            self.player.rect.bottom=sprite.rect.top
            self.n=0
            self.player.state='walk'
            self.can_fall = True
        else:
            self.player.y_v=C.r_v
            self.player.rect.top=sprite.rect.bottom
            if self.can_fall:
                self.player.state='fall'
            else:
                self.player.state='fall2'
        return self.n,self.can_fall

    def check_will_fall(self,sprite):
        sprite.rect.y+=1
        collided=pygame.sprite.spritecollideany(self.player,self.ground_item_group)
        if not collided and sprite.state!='jump' and sprite.state!='jump2':
            if self.can_fall:
                sprite.state='fall'
            else:
                sprite.state = 'fall2'
        sprite.rect.y-=1

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.player.image,self.player.rect)
        self.info.draw(surface)
        self.enemy_group.draw(surface)

    def check_die(self):
        collided = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if collided:
            self.player.rect.x=C.x_3  
            self.player.rect.y=C.y_3   
            self.player.state='walk'

    def check_end(self):
        collided = pygame.sprite.spritecollideany(self.player, self.ending)
        if collided:
            self.finished = True

class level4:
    def __init__(self):
        self.finished=False
        self.info=info.Info('level4')
        self.setup_background()
    def setup_background(self):
        self.background=setup.PER['背景']     #将引用的背景图名字写入
        self.viewport=setup.SCREEN.get_rect()
    def update(self,surface,keys,n):
        self.n=n

        surface.blit(self.background,self.viewport)

        self.info.update()
        self.info.draw(surface)
        return self.n







