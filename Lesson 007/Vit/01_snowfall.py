# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
from random import uniform
sd.resolution = (1200, 700)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

n = 3


class Snowflake:
    def __init__(self):

        self.color = sd.COLOR_YELLOW
        self.fallen_flakes = 0
        self.fallen_number_list = []
        self.new_list_typle = []


    def get_flakes(self, count):
        self.x_list = []  # создаем пустой список координа х
        self.y_list = []  # создаем пустой список координат у
        self.a_list = []
        self.b_list = []
        self.c_list = []
        self.l_list = []

        new_list = []
        self.new_new_list = []
        list_flake = []

        for _ in range(1, count + 1):
            y_points = sd.random_number(500, 700)  # создаем рандомные координаты х
            x_points = sd.random_number(100, 900)  # создаем рандомные координаты у
            lengths = sd.random_number(10, 40)  # рандомный размер самой снежинки
            factor_aa = round(uniform(0.3, 0.7), 2)  # рандомное место ответвления лучиков
            factor_bb = round(uniform(0.25, 0.45), 2)  # рандомная длина лучиков
            factor_cc = sd.random_number(10, 100)  # рандомный угол отклонения лучиков
            list_flake.append(_)

            new_list.append(_)
            new_list.append(x_points)
            new_list.append(y_points)
            new_list.append(factor_aa)
            new_list.append(factor_bb)
            new_list.append(factor_cc)
            new_list.append(lengths)

            # print('new_list=', new_list)
            self.new_new_list.append(new_list)

            tuple1 = tuple(new_list)
            self.new_list_typle.append(tuple1)
            tuple1 = ()
            new_list = []

            # print('nnl=', new_new_list)

        x2_list = ()
        x2_list = tuple(
            self.x_list)  # создаем кортеж координат x, для повторого "сброса" каждой снежинки с той же координаты x что и в
        y2_list = ()
        y2_list = tuple(
            self.y_list)  # создаем кортеж координат у, для повторого "сброса" каждой снежинки с той же высоты что и в
        # первый раз
        return list_flake

    def clear_previous_picture(self, i):
        self.center = sd.get_point(int(self.new_new_list[i-1][1]), int(self.new_new_list[i-1][2]))
        # self.center = sd.get_point(int(self.x_list[i]), int(self.y_list[i]))
        self.color = sd.background_color
        # sd.snowflake(center=self.center[i], length=self.l_list[i], color=self.color, factor_a=self.a_list[i],
        #              factor_b=self.b_list[i], factor_c=self.c_list[i])
        sd.snowflake(center=self.center, length=self.new_new_list[i-1][6], color=self.color, factor_a=self.new_new_list[i-1][3],
                     factor_b=self.new_new_list[i-1][4], factor_c=self.new_new_list[i-1][5])


    def move(self, i):
        self.new_new_list[i-1][2] -= 40  # падаем на 10 пикс.
        # print(self.y_list)
        # x_list += sd.random_number(-50, 50)  # изменяет Х координату случайно от -50 до 50
        if self.new_new_list[i - 1][2] < self.new_new_list[i - 1][6]:  # проверка упала ли снежинка
            self.fallen_flakes += 1
            self.fallen_number_list.append(i)


    def draw(self, i):
        self.center = sd.get_point(int(self.new_new_list[i-1][1]), int(self.new_new_list[i-1][2]))
        self.color = sd.COLOR_YELLOW
        sd.snowflake(center=self.center, length=self.new_new_list[i-1][6], color=self.color, factor_a=self.new_new_list[i-1][3],
                     factor_b=self.new_new_list[i-1][4], factor_c=self.new_new_list[i-1][5])


    # def can_fall(self, i):
    #     if self.y_list[i] < self.l_list[i]:  # проверка упала ли снежинка
    #         None
    #     else:
    #         return True

    def get_fallen_flakes(self):
        # if self.new_new_list[i-1][2] < self.new_new_list[i-1][6]:  # проверка упала ли снежинка
        #     None

        return self.fallen_flakes


    def append_flakes(self):
        for rr in self.fallen_number_list:
            self.new_new_list[rr-1][2] = self.new_list_typle[rr-1][2]

        self.fallen_flakes = 0
        self.fallen_number_list = []



# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

flake = Snowflake()  # создать список снежинок
flakes = flake.get_flakes(count= n)

while True:
    for flakeq in flakes:
        flake.clear_previous_picture(i = flakeq)
        flake.move(i = flakeq)
        flake.draw(i = flakeq)
    fallen_flakes = flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flake.append_flakes()  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break



sd.pause()
