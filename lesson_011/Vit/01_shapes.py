# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

def get_polygon(n):
    print(n)
    def draw_triangle(point, angle, length):
        point1 = point
        for line_n in range(1, n): #заменить n на "n+1" и убрать строку 24 чтобы рисовалось векторами,
                                   # но может быть нестыковка первого и последнего вектора
            line = sd.get_vector(start_point=point1, angle=(angle + ((360 * line_n)/n)), length=length, width=1)
            line.draw()
            point1 = line.end_point
        line = sd.line(start_point = point1, end_point = point, width=1)

    return draw_triangle

draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(400, 200), angle=13, length=100)

sd.pause()
