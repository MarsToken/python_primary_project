# -*-coding:utf-8 -*-
# Author:王茂波
# function:主入口函数
import pygame
import time
from pygame.locals import *
import aircraft_fight.aircraft_project.python_code.ClassModel as model
import aircraft_fight.aircraft_project.python_code.Constants as Contants


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

    enemy_0 = model.EnemyPlane(screen)

    while True:
        # 背景，坐标
        screen.blit(background, (Contants.COORDINATE_X, Contants.COORDINATE_Y))
        player.display()
        enemy_0.display()
        enemy_0.move_free()
        enemy_0.fire()
        # 更新
        pygame.display.update()
        detect_keyboard(player)
        # 降低cpu使用率
        time.sleep(Contants.DIFFICULT_LEVEL)


if __name__ == '__main__':
    main()
