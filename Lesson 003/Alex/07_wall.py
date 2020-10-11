# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x1 = 0
y1 = 0
x2 = 100
y2 = 50
for a in range(7):
    point_1 = sd.get_point(x1, y1)
    point_2 = sd.get_point(x2, y2)
    x1 += 100
    x2 += 100
    sd.rectangle(left_bottom=point_1, right_top=point_2, width=1)

x3 = -50
y3 = 50
x4 = 50
y4 = 100
for b in range(7):
    point_3 = sd.get_point(x3, y3)
    point_4 = sd.get_point(x4, y4)
    x3 += 100
    x4 += 100
    sd.rectangle(left_bottom=point_3, right_top=point_4, width=1)

x5 = 0
y5 = 100
x6 = 100
y6 = 150
for c in range(7):
    point_5 = sd.get_point(x5, y5)
    point_6 = sd.get_point(x6, y6)
    x5 += 100
    x6 += 100
    sd.rectangle(left_bottom=point_5, right_top=point_6, width=1)
sd.pause()


#for x in range(100, 1001, 100):
#    for y in range(100, 301, 100):
#        point = sd.get_point(x, y)
#        bubble(point=point, step=5)