# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1800, 1000)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

def draw_branches(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point

angle_0 = 90
length_0 = 200
point_0 = sd.get_point(400, 5)

next_angle = angle_0
next_length = length_0
next_point = point_0
next_angle2 = angle_0
next_point2 = point_0

# while next_length > 1:
#     next_point = draw_branches(point=next_point, angle=next_angle, length=next_length)
#     next_point2 = draw_branches(point=next_point2, angle=next_angle2, length=next_length)
#     next_angle = next_angle - 30
#     next_angle2 = next_angle2 + 30
#     next_length = next_length * .75
# раскомментировать для работы


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

angle_2 = 90
length_2 = 200
delta_2 = 30
point_2 = sd.get_point(900, 5)
def draw_branches2(point1, point2, angle1, angle2, length, delta):
    if length < 10:
        return
    v2_1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=3)
    v2_1.draw()
    next_point1 = v2_1.end_point
    next_angle1 = angle1 - delta
    v2_2 = sd.get_vector(start_point=point2, angle=angle2, length=length, width=3)
    v2_2.draw()
    next_point2 = v2_2.end_point
    next_angle2 = angle2 + delta
    next_length = length * .75
    draw_branches2(point1=next_point1, point2=next_point2, angle1=next_angle1, angle2=next_angle2, length=next_length, delta=delta)


# draw_branches2(point1=point_2, point2=point_2, angle1=angle_2, angle2=angle_2, length=200, delta=delta_2)
# !!!раскомментировать для работы!!!


# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

root_point = sd.get_point(900, 30)
def draw_branches3(start_point, angle, length):
    delta = 30
    if length < 8:
        return
    v2_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v2_1.draw()
    next_point1 = v2_1.end_point
    next_angle1 = angle - delta
    v2_2 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v2_2.draw()
    next_point2 = v2_2.end_point
    next_angle2 = angle + delta
    next_length = length * .75
    draw_branches3(start_point=next_point1, angle=next_angle1, length=next_length)
    draw_branches3(start_point=next_point2, angle=next_angle2, length=next_length)

# draw_branches3(start_point=root_point, angle=90, length=200)
# !!!раскомментировать для работы!!!


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# def draw_branches4(start_point, angle, length):
#     delta = sd.random_number(a=30, b=40)
#     if length < 3:
#         return
#     v2_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v2_1.draw()
#     next_point1 = v2_1.end_point
#     next_angle1 = angle - delta
#     v2_2 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v2_2.draw()
#     next_point2 = v2_2.end_point
#     next_angle2 = angle + delta
#     k = (sd.random_number(a=80, b=120)) * (0.01)
#     print(k)
#     next_length = length * .75 * k
#     draw_branches3(start_point=next_point1, angle=next_angle1, length=next_length)
#     draw_branches3(start_point=next_point2, angle=next_angle2, length=next_length)
#
# draw_branches4(start_point=root_point, angle=90, length=200)

angle_4 = 90
length_4 = 200
delta1 = sd.random_number(a=30, b=40)
delta2 = sd.random_number(a=30, b=40)
point_4 = sd.get_point(900, 5)

def draw_branches4(point, angle, length1, length2, delta1, delta2):
    if length1 < 4 and length2 < 4:
        return
    v2_1 = sd.get_vector(start_point=point, angle=angle, length=length1, width=1)
    v2_1.draw()
    delta1 = sd.random_number(a=30, b=40)
    next_point1 = v2_1.end_point
    next_angle1 = angle - delta1
    k1 = (sd.random_number(a=80, b=120)) * (0.01)
    next_length1 = length1 * .75 * k1
    v2_2 = sd.get_vector(start_point=point, angle=angle, length=length2, width=1)
    v2_2.draw()
    delta2 = sd.random_number(a=30, b=40)
    next_point2 = v2_2.end_point
    next_angle2 = angle + delta2
    k2 = (sd.random_number(a=80, b=120)) * (0.01)
    next_length2 = length2 * .75 * k2
    draw_branches4(point=next_point1, angle=next_angle1, length1=next_length1, length2=next_length2, delta1=delta1, delta2=delta2)
    draw_branches4(point=next_point2, angle=next_angle2, length1=next_length1, length2=next_length2, delta1=delta1, delta2=delta2)

draw_branches4(point=point_4, angle=angle_4, length1=200, length2=200, delta1=delta1, delta2=delta2)


sd.pause()


