# -*- coding: utf-8 -*-

def koordinate(n):
    import simple_draw as sd
    from random import uniform
    # global x_list
    x_list = []  # создаем пустой список координа х
    y_list = []  # создаем пустой список координат у
    a_list = []
    b_list = []
    c_list = []
    l_list = []

    for _ in range(n):
        y_points = sd.random_number(500, 700)  # создаем рандомные координаты х
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

    x2_list = ()
    x2_list = tuple(x_list)  # создаем кортеж координат x, для повторого "сброса" каждой снежинки с той же координаты x что и в
    y2_list = ()
    y2_list = tuple(y_list)     # создаем кортеж координат у, для повторого "сброса" каждой снежинки с той же высоты что и в
    # первый раз
    return x_list, y_list, a_list, b_list, c_list, l_list, y2_list, x2_list

def snowdraw(color, n, x_list, y_list, a_list, b_list, c_list, l_list, i):
    import simple_draw as sd
    sd.start_drawing()
    for i in range(n):
        point = sd.get_point(int(x_list[i]), int(y_list[i]))  # задаем координаты
        sd.snowflake(center=point, length=l_list[i], color=color, factor_a=a_list[i], factor_b=b_list[i],
              factor_c=c_list[i])  # вызываем ф-цию отрисовки снежинки цветом color
        sd.finish_drawing()

def snowfly(x_list, y_list, i):
    import simple_draw as sd
    y_list[i] -= 50  # падаем на 10 пикс.
    # x_list[i] += .5
    x_list[i] += sd.random_number(-50, 50)    # изменяет Х координату случайно от -50 до 50

def issnowdown(color, n, x_list, y_list, a_list, b_list, c_list, l_list, i):
    import simple_draw as sd
    sd.start_drawing()
    if y_list[i] < l_list[i]:               # проверка упала ли снежинка
        # y_last = l_list[i]
        # point =sd.get_point(x_list[i], y_last)
        # sd.snowflake(center=point, length=l_list[i], color=color, factor_a=a_list[i], factor_b=b_list[i],
        #       factor_c=c_list[i])  # вызываем ф-цию отрисовки снежинки цветом COLOR на земле
        return True

def delsnow(x_list, y_list, a_list, b_list, c_list, l_list, i):
    import simple_draw as sd
    sd.start_drawing()
    point = sd.get_point(int(x_list[i]), int(y_list[i]))  # задаем координаты
    sd.snowflake(center=point, length=l_list[i], color=sd.background_color, factor_a=a_list[i], factor_b=b_list[i],
                 factor_c=c_list[i])  # вызываем ф-цию отрисовки снежинки цветом color
    sd.finish_drawing()

def renewsnow(x_list, x2_list, y_list, y2_list, i):
    x_list[i] = x2_list[i]
    y_list[i] = y2_list[i]
    return x_list, y_list
