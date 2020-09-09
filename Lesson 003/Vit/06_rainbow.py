# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
y1 = 50
y2 = 450
for xxx in rainbow_colors:
    point1 = sd.get_point(50, y1)
    point2 = sd.get_point(350, y2)
    sd.line(point1, point2, color=xxx, width=4)
    y1 -= 5
    y2 -= 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

r = 100
for xxx in rainbow_colors:
    point3 = sd.get_point(200, 0)
    sd.circle(point3, radius=r, color=xxx, width=4)
    r -=5
sd.pause()
