# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (600, 600)
point1 = sd.get_point(0, 0)
point2 = sd.get_point(280, 315)
point3 = sd.get_point(320, 315)
point_ellipse1 = sd.get_point(235, 250)
point_ellipse2 = sd.get_point(365, 350)
line_point1 = sd.get_point(270, 290)
line_point2 = sd.get_point(280, 280)
line_point3 = sd.get_point(320, 280)
line_point4 = sd.get_point(330, 290)

# Написать функцию отрисовки смайлика в произвольной точке экрана

def smile(point, color=sd.COLOR_YELLOW):
        radius2 = 5
        sd.circle(center_position=point2, radius=radius2, width=1)
        sd.circle(center_position=point3, radius=radius2, width=1)
        sd.line(start_point=line_point1, end_point=line_point2, width=1)
        sd.line(start_point=line_point2, end_point=line_point3, width=1)
        sd.line(start_point=line_point3, end_point=line_point4, width=1)
        sd.ellipse(left_bottom=point_ellipse1, right_top=point_ellipse2, width=1)


smile(point=point1)

# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.pause()
