# -*-coding:utf-8 -*-
# Author:王茂波
# function:各种类数据模型
import random
import pygame
import aircraft_fight.aircraft_project.python_code.Constants as Constants

type_image_enemy = ('../feiji/enemy0.png',
                    '../feiji/enemy1.png',
                    '../feiji/enemy2.png')
list_image_death_aim = (('../feiji/enemy0_down1.png',
                         '../feiji/enemy0_down2.png',
                         '../feiji/enemy0_down3.png',
                         '../feiji/enemy0_down4.png'),
                        ('../feiji/enemy1_down1.png',
                         '../feiji/enemy1_down2.png',
                         '../feiji/enemy1_down3.png',
                         '../feiji/enemy1_down4.png'),
                        ('../feiji/enemy2_down1.png',
                         '../feiji/enemy2_down2.png',
                         '../feiji/enemy2_down3.png',
                         '../feiji/enemy2_down4.png'))
type_size = ({'width': Constants.EMENY0_WIDTH,
              'height': Constants.EMENY0_HEIGHT},
             {'width': Constants.EMENY1_WIDTH,
              'height': Constants.EMENY1_HEIGHT},
             {'width': Constants.EMENY2_WIDTH,
              'height': Constants.EMENY2_HEIGHT})
type_image_enemy_bullet = ('../feiji/bullet1.png',
                           '../feiji/bullet2.png',
                           '../feiji/bullet.png')


class BasePlane:
    # 类属性，记录敌机的信息
    list_enemy_plant = []
    list_player_plant = []

    def __init__(self, screen, x, y, w, h, image_name, identify):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = pygame.image.load(image_name)
        self.screen = screen
        self.bullet_list = []
        self.main_time = 0  # 主线程循环次数
        self.death_index = 0  # 死亡动画帧数
        self.is_dead = False
        self.identify = identify  # 身份，1为英雄 其他为敌机

    def display(self):
        # 如果死了就不用判断了，直到死亡动画结束
        if self.is_dead or self.is_hint():
            self.dead()
        else:
            self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.isBeyond():  # list删除元素，漏掉了上一个
                self.bullet_list.remove(bullet)

    # 敌我相撞 或 被子弹打中
    def is_hint(self):
        for _player in BasePlane.list_player_plant:
            _player_left = _player.x
            _player_top = _player.y
            _player_right = _player.x + Constants.PLAYER_WIDTH
            _player_bottom = _player.y + Constants.PLAYER_HEIGHT
            for _enemy in BasePlane.list_enemy_plant:
                _enemy_left = _enemy.x
                _enemy_top = _enemy.y
                _enemy_right = _enemy.x + type_size[_enemy.type]['width']
                _enemy_bottom = _enemy.y + type_size[_enemy.type]['height']
                if _player_left < _enemy_right and _enemy_left < _player_right and _player_top < _enemy_bottom and _enemy_top < _player_bottom:
                    print("敌我相撞")
                    _player.is_dead = True
                    _enemy.is_dead = True
                    return True

    def fire(self):
        pass

    def dead(self, list_image):
        if self.identify == 1:
            self.screen.blit(pygame.image.load(list_image[self.death_index]), (self.x, self.y))
        else:
            self.screen.blit(pygame.image.load(list_image[self.type][self.death_index]),
                             (self.x, self.y))
        self.main_time += 1
        if self.main_time == 5:  # 每个爆炸图片显示5*0.01s，太长会有bug_is_hint：true-false
            self.main_time = 0
            self.death_index += 1
        if self.death_index > 3:
            self.death_index = 0
            # self.is_dead = False
            if self in BasePlane.list_player_plant:
                BasePlane.list_player_plant.remove(self)
            list_temp = []
            if self in BasePlane.list_enemy_plant:
                list_temp.append(self)
            for temp in list_temp:
                BasePlane.list_enemy_plant.remove(temp)
            self.start = False
            # time.sleep(1)
            # exit()


class Player(BasePlane):
    def __init__(self, screen):
        super().__init__(screen,
                         Constants.INITIAL_PLAYER_X,
                         Constants.INITIAL_PLATER_Y,
                         Constants.PLAYER_WIDTH,
                         Constants.PLAYER_HEIGHT,
                         '../feiji/hero1.png', 1)
        BasePlane.list_player_plant.clear()
        BasePlane.list_player_plant.append(self)
        self.score = 0
        self.start = False

    def move_left(self):
        self.x -= Constants.UNIT_LEN * Constants.PLAYER_MOVE_FACTOR
        self.__move_beyond()

    def move_right(self):
        self.x += Constants.UNIT_LEN * Constants.PLAYER_MOVE_FACTOR
        self.__move_beyond()

    def move_top(self):
        self.y -= Constants.UNIT_LEN * Constants.PLAYER_MOVE_FACTOR
        self.__move_beyond()

    def move_bottom(self):
        self.y += Constants.UNIT_LEN * Constants.PLAYER_MOVE_FACTOR
        self.__move_beyond()

    # 越界判断
    def __move_beyond(self):
        if self.x > Constants.BACKGROUND_WIDTH - Constants.PLAYER_WIDTH:
            self.x = Constants.BACKGROUND_WIDTH - Constants.PLAYER_WIDTH
        elif self.x < 0:
            self.x = 0
        if self.y > Constants.BACKGROUND_HEIGHT - Constants.PLAYER_HEIGHT:
            self.y = Constants.BACKGROUND_HEIGHT - Constants.PLAYER_HEIGHT
        elif self.y < 0:
            self.y = 0

    def fire(self):
        self.bullet_list.append(PlayerBullet(self.screen, self.x, self.y))

    def is_hint(self):
        super().is_hint()
        for enemy_plane in BasePlane.list_enemy_plant:
            for bullet in enemy_plane.bullet_list:
                x = bullet.x
                y = bullet.y
                if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                    self.is_dead = True
                    return True
        return False

    def dead(self):
        list_image = ['../feiji/hero_blowup_n1.png',
                      '../feiji/hero_blowup_n2.png',
                      '../feiji/hero_blowup_n3.png',
                      '../feiji/hero_blowup_n4.png']
        super().dead(list_image)
        # 死了之后清空对象clear
        # self = None


class EnemyPlane(BasePlane):
    def __init__(self, screen, type):
        # 根据类型，定敌机的各种参数，比如图片，宽高尺寸等
        super().__init__(screen,
                         Constants.COORDINATE_X,
                         Constants.COORDINATE_Y,
                         type_size[type]['width'],
                         type_size[type]['height'],
                         type_image_enemy[type], -1)
        self.direction = 'right'
        self.type = type  # 敌机类型
        BasePlane.list_enemy_plant.append(self)
        print("1=======%d" % len(BasePlane.list_enemy_plant))

    def display(self):
        super().display()
        self.__lose()

    def move_free(self):
        self.y += Constants.UNIT_LEN * Constants.ENEMY_MOVE_FACTOR
        if self.direction == 'right':
            self.x += (Constants.UNIT_LEN * Constants.ENEMY_MOVE_FACTOR)
        elif self.direction == 'left':
            self.x -= (Constants.UNIT_LEN * Constants.ENEMY_MOVE_FACTOR)
        if self.x > Constants.BACKGROUND_WIDTH - type_size[self.type]['width']:
            self.direction = 'left'
            self.x = Constants.BACKGROUND_WIDTH - type_size[self.type]['width']
        elif self.x < 0:
            self.direction = 'right'
            self.x = 0

    def fire(self):
        rad = random.randint(0, Constants.BASE_POSSIBILITY * Constants.ENEMY_DENSITY)
        if rad == 0:
            self.bullet_list.append(EnemyBullet(self.screen, self.type, self.x, self.y))

    def is_hint(self):
        super().is_hint()
        for player in BasePlane.list_player_plant:
            for bullet in player.bullet_list:
                x = bullet.x
                y = bullet.y
                if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                    self.is_dead = True;
                    if self.type == 0:
                        player.score += Constants.ENEMY0_DEATH_SCORE
                    elif self.type == 1:
                        player.score += Constants.ENEMY1_DEATH_SCORE
                    elif self.type == 2:
                        player.score += Constants.ENEMY2_DEATH_SCORE
                    # 击中敌机，我的子弹就消失
                    player.bullet_list.remove(bullet)
                    return True
        return False

    def dead(self):
        super().dead(list_image_death_aim)

    def __lose(self):
        if self.y > Constants.BACKGROUND_HEIGHT:
            if self in BasePlane.list_enemy_plant:
                BasePlane.list_enemy_plant.remove(self)


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
        self.y -= Constants.UNIT_LEN * Constants.PLAYER_BULLET_MOVE_FACTOR

    def isBeyond(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen, type, x, y):
        super().__init__(screen,
                         x + type_size[type]['width'] / 2,
                         y + type_size[type]['height'],
                         type_image_enemy_bullet[type])

    def move(self):
        self.y += Constants.UNIT_LEN * Constants.ENEMY_BULLET_MOVE_FACTOR

    def isBeyond(self):
        if self.y > Constants.BACKGROUND_HEIGHT - Constants.EMEMY0_BULLET_HEIGHT:
            return True
        else:
            return False
