# -*-coding:utf-8 -*-
# Author:王茂波
# function:各种类数据模型
import random
import pygame
import time
import aircraft_fight.aircraft_project.python_code.Constants as Constants


class BasePlane:
    # 类属性，记录敌机的信息
    list_enemy_plant = []
    list_player_plant = []

    def __init__(self, screen, x, y, w, h, image_name):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = pygame.image.load(image_name)
        self.screen = screen
        self.bullet_list = []
        self.main_time = 0
        self.death_index = 0
        self.is_dead = False

    def display(self):
        # 如果死了就不用判断了，直到死亡动画结束
        if self.is_dead or self.__is_hint():
            self.dead()
        else:
            self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.isBeyond():  # list删除元素，漏掉了上一个
                self.bullet_list.remove(bullet)

    def __is_hint(self, list_plant):
        for enemy_plane in list_plant:
            for bullet in enemy_plane.bullet_list:
                x = bullet.x
                y = bullet.y
                if self.x < x < self.x + self.width and self.y < y < self.y + self.width:
                    self.is_dead = True;
                    return True
        return False

    def fire(self):
        pass

    def dead(self):
        pass


class Player(BasePlane):
    def __init__(self, screen):
        super().__init__(screen,
                         Constants.INITIAL_PLAYER_X,
                         Constants.INITIAL_PLATER_Y,
                         Constants.PLATER_WIDTH,
                         Constants.PLATER_HEIGHT,
                         '../feiji/hero1.png')
        BasePlane.list_player_plant.append(self)

    def move_left(self):
        self.x -= Constants.UNIT_LEN

    def move_right(self):
        self.x += Constants.UNIT_LEN

    def move_top(self):
        self.y -= Constants.UNIT_LEN

    def move_bottom(self):
        self.y += Constants.UNIT_LEN

    def fire(self):
        self.bullet_list.append(PlayerBullet(self.screen, self.x, self.y))

    def __is_hint(self):
        return super().__is_hint(BasePlane.list_enemy_plant)

    def dead(self):
        list_image = ['../feiji/hero_blowup_n1.png',
                      '../feiji/hero_blowup_n2.png',
                      '../feiji/hero_blowup_n3.png',
                      '../feiji/hero_blowup_n4.png']
        self.screen.blit(pygame.image.load(list_image[self.death_index]), (self.x, self.y))
        self.main_time += 1
        if self.main_time == 5:  # 每个爆炸图片显示5*0.01s，太长会有bug_is_hint：true-false
            self.main_time = 0
            self.death_index += 1
        if self.death_index > 3:
            self.death_index = 0
            self.is_dead = False
            time.sleep(1)
            # exit()


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen,
                         Constants.COORDINATE_X,
                         Constants.COORDINATE_Y,
                         Constants.EMENY0_WIDTH,
                         Constants.EMENY0_HEIGHT,
                         '../feiji/enemy0.png')
        self.direction = 'right'
        BasePlane.list_enemy_plant.append(self)

    def move_free(self):
        if self.direction == 'right':
            self.x += (Constants.UNIT_LEN / 2)
        elif self.direction == 'left':
            self.x -= (Constants.UNIT_LEN / 2)
        if self.x > Constants.BACKGROUND_WIDTH - Constants.EMENY0_WIDTH:
            self.direction = 'left'
            self.x = Constants.BACKGROUND_WIDTH - Constants.EMENY0_WIDTH
        elif self.x < 0:
            self.direction = 'right'
            self.x = 0

    def fire(self):
        rad = random.randint(0, 100)
        if rad == 0 or rad == 10:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet:
    def __init__(self, screen, x, y, image_name):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass

    def isBeyond(self):
        pass


class PlayerBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super().__init__(screen, x + 40, y - 20, '../feiji/bullet.png')

    def move(self):
        self.y -= Constants.UNIT_LEN / 2

    def isBeyond(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super().__init__(screen,
                         x + Constants.EMENY0_WIDTH / 2,
                         y + Constants.EMENY0_HEIGHT,
                         '../feiji/bullet1.png')

    def move(self):
        self.y += Constants.UNIT_LEN / 2

    def isBeyond(self):
        if self.y > Constants.BACKGROUND_HEIGHT - Constants.EMEMY0_BULLET_HEIGHT:
            return True
        else:
            return False
