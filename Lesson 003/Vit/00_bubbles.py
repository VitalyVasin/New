# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point1 = sd.get_point(200, 200)
radius = 50

for _ in range(3):
    radius += 5
    sd.circle(center_position=point1, radius=radius, width=2)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point1, radius=radius, width=2)

bubble(point=point1, step=20)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    point1 = sd.get_point(x, 100)
    bubble(point=point1, step=5)

# Нарисовать три ряда по 10 пузырьков

for x in range(100, 1001, 100):
    for y in range(100, 401, 100):
        point1 = sd.get_point(x, y)
        bubble(point=point1, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point1 = sd.random_point()
    bubble(point=point1, step=5)

sd.pause()


