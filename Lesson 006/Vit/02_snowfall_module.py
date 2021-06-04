# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall_engine import koordinate, snowdraw, snowfly, issnowdown, delsnow, renewsnow

sd.resolution = (1000, 700)

qua = int(input('Введите количество снежинок: '))

x_list, y_list, a_list, b_list, c_list, l_list, y2_list, x2_list = koordinate(n=qua)
color = sd.COLOR_WHITE

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
while True:
    for i in range(qua):
        snowdraw(color=sd.background_color, n=qua, x_list=x_list, y_list=y_list, a_list=a_list, b_list=b_list,\
                 c_list=c_list, l_list=l_list, i=i)    #  нарисовать_снежинки_цветом(color=sd.background_color)
        snowfly(x_list=x_list, y_list=y_list, i=i) #  сдвинуть_снежинки()
        snowdraw(color=color, n=qua, x_list=x_list, y_list=y_list, a_list=a_list, b_list=b_list, c_list=c_list,\
                 l_list=l_list, i=i)              #  нарисовать_снежинки_цветом(color)
        if issnowdown(color=color, n=qua, x_list=x_list, y_list=y_list, a_list=a_list, b_list=b_list, c_list=c_list,\
                   l_list=l_list, i=i):  #  если есть номера_достигших_низа_экрана() то
            delsnow(x_list=x_list, y_list=y_list, a_list=a_list, b_list=b_list,\
                     c_list=c_list, l_list=l_list, i=i) #       удалить_снежинки(номера)
            renewsnow(x_list=x_list, x2_list=x2_list, y_list=y_list, y2_list=y2_list, i=i) #       создать_снежинки(count)
        sd.sleep(0.1)
    if sd.user_want_exit():
        break
