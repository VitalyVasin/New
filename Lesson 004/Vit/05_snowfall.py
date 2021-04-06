# -*- coding: utf-8 -*-

import simple_draw as sd
from random import uniform

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

sd.resolution = (1000, 700)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

n = 20  # количество снежинок (чем их больше тех хуже анимация)
x_list = []  # создаем пустой список координа х
y_list = []  # создаем пустой список координат у
a_list = []
b_list = []
c_list = []
l_list = []

for _ in range(n):
    y_points = sd.random_number(500, 1650)  # создаем рандомные координаты х
    x_points = sd.random_number(100, 900)  # создаем рандомные координаты у
    x_list.append(x_points)  # запись координат х в список (на последнее место)
    y_list.append(y_points)  # запись координат у в список (на последнее место)
    lengths = sd.random_number(10, 40)  # рандомный размер самой снежинки
    factor_aa = round(uniform(0.3, 0.7), 2)  # рандомное место ответвления лучиков
    factor_bb = round(uniform(0.25, 0.45), 2)  # рандомная длина лучиков
    factor_cc = sd.random_number(10, 100)  # рандомный угол отклонения лучиков
    l_list.append(lengths)  # запись координат размера снежинок в список
    a_list.append(factor_aa)  # запись значений мест для отвлетвления лучиков
    b_list.append(factor_bb)  # запись значений длины лучиков
    c_list.append(factor_cc)  # запись значений для угла отклонения лучков

y2_list = ()
y2_list = tuple(y_list)     # создаем кортеж координат у, для повторого "сброса" каждой снежинки с той же высоты что и в
# первый раз

sd.start_drawing()

def snowf(center, length, color, factor_a, factor_b, factor_c):  # ф-ция отрисовки снежинки
    sd.snowflake(center, length, color, factor_a, factor_b, factor_c)  # отрисовка

def snowfunc(length, factor_a, factor_b, factor_c):
    while True:
        for i in range(n):
            point = sd.get_point(x_list[i], y_list[i])  # задаем координаты
            fac_a = a_list[i]
            fac_b = b_list[i]
            fac_c = c_list[i]
            l_length = l_list[i]

            snowf(center=point, length=l_length, color=sd.background_color, factor_a=fac_a, factor_b=fac_b,
                  factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки цветом sd.background_color
            y_list[i] -= 10  # падаем на 10 пикс.
            # x_list[i] += .5
            # x_list[i] += sd.random_number(-50, 50)
            if y_list[i] < l_length:  # проверка упала ли снежинка
                y_last = l_length
                point =sd.get_point(x_list[i], y_last)
                snowf(center=point, length=l_length, color=sd.COLOR_WHITE, factor_a=fac_a, factor_b=fac_b,
                      factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки цветом COLOR_RED
                y_list[i] = y2_list[i]
            else:
                x_list[i] += sd.random_number(-50, 50)
            point1 = sd.get_point(x_list[i], y_list[i])
            snowf(center=point1, length=l_length, color=sd.COLOR_WHITE, factor_a=fac_a, factor_b=fac_b,
                  factor_c=fac_c)  # вызываем ф-цию отрисовки снежинки

            sd.finish_drawing()
            sd.sleep(0.01)

        if sd.user_want_exit():
            break
    # sd.clear_screen()
snowfunc(length=l_list[0], factor_a=a_list[0], factor_b=b_list[0], factor_c=c_list[0])
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


