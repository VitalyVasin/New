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

def triangle(point, angle, length, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=width)
    v3.draw()

def square (point, angle, length, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=width)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=width)
    v3.draw()
    sd.line(start_point=v3.end_point,end_point=point, width=width)

def pentagon (point, angle, length, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=width)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=width)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=width)
    v4.draw()
    sd.line(start_point=v4.end_point, end_point=point, width=width)

def hexagon (point, angle, length, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=width)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=width)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=width)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=width)
    v5.draw()
    sd.line(start_point=v5.end_point, end_point=point, width=width)

point_1 = sd.get_point(100, 100)
point_2 = sd.get_point(400, 100)
point_3 = sd.get_point(100, 400)
point_4 = sd.get_point(400, 400)
point_5 = sd.get_point(300, 300)

triangle(point=point_1, angle=18, length=150, width=2)
square(point=point_2, angle=28, length=150, width=2)
pentagon(point=point_3, angle=24, length=100, width=2)
hexagon(point=point_4, angle=10, length=100, width=2)

def figure (point, number_sides, angle, length, width):

    if number_sides == 3:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v1.draw()
        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
        v2.draw()
        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=width)
        v3.draw()
        print('It is triangle')

    if number_sides == 4:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v1.draw()
        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=width)
        v2.draw()
        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=width)
        v3.draw()
        sd.line(start_point=v3.end_point, end_point=point, width=width)
        print('It is square')


    if number_sides == 5:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v1.draw()
        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=width)
        v2.draw()
        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=width)
        v3.draw()
        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=width)
        v4.draw()
        sd.line(start_point=v4.end_point, end_point=point, width=width)
        print('It is pentagon')


    if number_sides == 6:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v1.draw()
        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=width)
        v2.draw()
        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=width)
        v3.draw()
        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=width)
        v4.draw()
        v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=width)
        v5.draw()
        sd.line(start_point=v5.end_point, end_point=point, width=width)
        print('It is hexagon')
    if number_sides > 6:
        print('Write number of sides from 3 to 6')
    if number_sides < 3:
        print('Write number of sides from 3 to 6')

figure(point=point_5, number_sides=4, angle=30, length=100, width=2)





sd.pause()


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


sd.pause()
