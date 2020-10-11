# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for y in range(0, 1000, 100):
    for x in range(0, 1000, 100):
        point_1 = sd.get_point(x, y)
        point_2 = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_bottom=point_1, color=sd.COLOR_RED, right_top=point_2, width=2)
        point_3 = sd.get_point(x - 50, y + 50)
        point_4 = sd.get_point(x + 50, y + 100)
        sd.rectangle(left_bottom=point_3, color=sd.COLOR_RED, right_top=point_4, width=2)

sd.pause()
