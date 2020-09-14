# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1200, 600)


for x in range(-250, 1251, 250):
    for y in range(0, 601, 120):
        left_bottom1 = sd.get_point(x, y)
        right_top1 = sd.get_point(x + 250, y + 60)
        sd.rectangle(left_bottom1, right_top1, color=sd.COLOR_BLACK, width=3)
        left_bottom2 = sd.get_point(x + 125, y + 60)
        right_top2 = sd.get_point(x + 375, y + 120)
        sd.rectangle(left_bottom2, right_top2, color=sd.COLOR_BLACK, width=3)

sd.pause()
