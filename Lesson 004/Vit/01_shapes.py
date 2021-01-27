# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

length = 200
angle = 0
# point = sd.get_point(800, 600)
point_trangle = sd.get_point(50, 380)
point_square = sd.get_point(350, 380)
point_5corner = sd.get_point(100, 50)
point_6corner = sd.get_point(400, 50)

def triangle(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=1)
    v3.draw()

def square(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=200, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=200, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=200, width=3)
    v4.draw()

def fivecorner(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=130, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=130, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=130, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=130, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=130, width=3)
    v5.draw()

def sixcorner(point, length, angle):
    v1 = sd.get_vector(start_point=point, angle=angle, length=120, width=1)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=120, width=1)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=120, width=1)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=120, width=1)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=120, width=1)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=120, width=1)
    v6.draw()

# triangle(point=point_trangle, length=length, angle=angle)
# # square(point=point_square, length=length, angle=angle)
# # fivecorner(point=point_5corner, length=length, angle=angle)
# sixcorner(point=point_6corner, length=length, angle=angle)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

point1 = sd.get_point(100, 100)
quantity = 7
# def draw_figure(point, lenght, angle, quantity, width):
#
#     for v in range(1, quantity+1, 1):
#
#         if v > 1:
#             r=round(((360 / quantity) * (v - 1)),0)
#             n = sd.get_vector(start_point=n.end_point, angle=r, length=lenght, width=width)
#             n.draw()
#
#         else:
#             n = sd.get_vector(start_point=point1, angle=angle, length=lenght, width=width)
#             n.draw()
# Функция выше работает, но начало-конец чуть чуть расходятся.

point2 = sd.get_point(200, 100)
quantity2 = 5
length2 = 200
angle2 = 10
width2 = 1

def draw_figure2(point, angle, length, quantity, width):

    for v in range(1, quantity2, 1):
        print(angle)
        angle = angle2 + (round(((360 / quantity2) * (v - 1)), 0))
        line_point = point
        n = sd.get_vector(start_point=line_point, angle=angle, length=length2, width=width2)
        n.draw()
        point = n.end_point
    rr = sd.line(start_point=n.end_point, end_point=point2, color=(255, 255, 0), width=width2)


# def draw_figure2(point, lenght, angle, quantity, width):
#     pointX = point
#     for v in range(1, quantity, 1):
#         n = sd.get_vector(start_point=pointX, angle=angle, length=length2, width=width)
#         n.draw()
#
#         angle = round(((360 / quantity) * v), 0)
#         pointX = n.end_point
#         print()
#     sd.line(start_point=pointX, end_point=point2, width=width2)

draw_figure2(point=point2, length=length2, angle=angle2, quantity=quantity2, width=width2)
sd.pause()