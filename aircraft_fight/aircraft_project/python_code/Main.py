# -*-coding:utf-8 -*-
# Author:王茂波
# function:主入口函数
import pygame
import time
from pygame.locals import *
import aircraft_fight.aircraft_project.python_code.ClassModel as model
import aircraft_fight.aircraft_project.python_code.Constants as Contants
import random


def detect_keyboard(player):  # 监听键盘
    for event in pygame.event.get():
        if event.type == QUIT:  # 退出键
            print('exit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                player.move_left()
                print('left')
            elif event.key == K_d or event.key == K_RIGHT:
                player.move_right()
                print('right')
            elif event.key == K_w or event.key == K_UP:
                player.move_top()
            elif event.key == K_s or event.key == K_DOWN:
                player.move_bottom()
            elif event.key == K_SPACE:
                player.fire()
                print('space')


def main():
    screen = pygame.display.set_mode((Contants.BACKGROUND_WIDTH, Contants.BACKGROUND_HEIGHT), 0, 32)
    background = pygame.image.load('../feiji/background.png')
    player = model.Player(screen)
    # 分数显示 初始化
    pygame.init()
    font = pygame.font.SysFont('arial', 16)
    while True:
        # random随机生成飞机对象
        result = random.randint(0, Contants.BASE_POSSIBILITY * Contants.ENEMY_DENSITY)
        if result == 0 or result == 1 or result == 2:
            model.EnemyPlane(screen, result)
        # 背景，坐标
        screen.blit(background, (Contants.COORDINATE_X, Contants.COORDINATE_Y))
        for emery in model.BasePlane.list_enemy_plant:
            emery.display()
            emery.move_free()
            emery.fire()
        player.display()
        name_surface = font.render('score:%d' % player.score, True, (0, 0, 0), (255, 255, 255))
        screen.blit(name_surface, (10, 10))
        # 更新
        pygame.display.update()
        detect_keyboard(player)
        # 降低cpu使用率
        time.sleep(Contants.DIFFICULT_LEVEL)


if __name__ == '__main__':
    main()
