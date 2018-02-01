# -*-coding:utf-8 -*-
# Author:王茂波
# 工厂方法模式

class CarStore:
    # 创建所需要的对象
    def __init__(self):
        self.factory = Factory()

    def order(self, type):
        return self.factory.buy_car_by_type(type)


class Factory:
    def buy_car_by_type(self, type):
        if type == '索纳塔':
            print('索纳塔')
            return Suonata()
        elif type == '明图':
            print('明图')
            return Mingtu()
        elif type == 'Ix35':
            print('Ix35')
            return Ix35()


class Car(object):
    def remove(self):
        print('车在移动...')

    def music(self):
        print('正在听音乐...')

    def stop(self):
        print('车在停止...')


class Suonata(Car):
    def music(self):
        print('索纳塔听音乐')


class Mingtu(Car):
    def music(self):
        print('明图听音乐')


class Ix35(Car):
    def music(self):
        print('Ix35听音乐')


car_store = CarStore()
car = car_store.order('Ix35')
car.music()
