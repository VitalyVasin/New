# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (600, 600)



# Написать функцию отрисовки смайлика в произвольной точке экрана

def smile(x, y):
        point2 = sd.get_point(x, y)
        point3 = sd.get_point(x + 40, y)
        point_ellipse1 = sd.get_point(x - 50, y - 65)
        point_ellipse2 = sd.get_point(x + 90, y + 35)
        line_point1 = sd.get_point(x - 10, y - 25)
        line_point2 = sd.get_point(x, y - 35)
        line_point3 = sd.get_point(x + 40, y - 35)
        line_point4 = sd.get_point(x + 50, y - 25)
        radius2 = 5
        sd.circle(center_position=point2, radius=radius2, width=3)
        sd.circle(center_position=point3, radius=radius2, width=3)
        sd.line(start_point=line_point1, end_point=line_point2, width=3)
        sd.line(start_point=line_point2, end_point=line_point3, width=3)
        sd.line(start_point=line_point3, end_point=line_point4, width=3)
        sd.ellipse(left_bottom=point_ellipse1, right_top=point_ellipse2, width=3)

for _ in range(10):
        x = sd.random_number(0, 600)
        y = sd.random_number(0, 600)
        smile(x=x, y=y)


# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.pause()
