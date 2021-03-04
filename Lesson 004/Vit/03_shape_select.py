# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_figure(point, angle, length, quantity, width):
    point1=point
    for v in range(1, quantity, 1):
        angle2 = angle + (round(((360 / quantity) * (v - 1)), 0))
        line_point = point
        n = sd.get_vector(start_point=line_point, angle=angle2, length=length, width=width)
        n.draw()
        point = n.end_point
    rr = sd.line(start_point=n.end_point, end_point=point1, color=(255, 255, 0), width=width)

def enter_shape():
    point2 = sd.get_point(200, 100)
    point = point2
    length2 = 200
    angle2 = 10
    width2 = 1
    quantity2 = 0
    input_text = input ("0 : Треугольник, \n1 : Квадрат, \n2 : Пятиугольник, \n3 : Шестиугольник \nВозможные фигуры: ")
    is_process = False
    try:
        test_number = int(input_text)
        print("Это правильный ввод! Ваше счастливое число: ", test_number)
        if test_number == 0:
            quantity2 = 3
        elif test_number == 1:
            quantity2 = 4
        elif test_number == 2:
            quantity2 = 5
        elif test_number == 3:
            quantity2 = 6
        else:
            print("Не корректный ввод!")
            quantity2 = -1
        if quantity2 != -1:
            draw_figure(point=point2, angle=angle2, length=length2, quantity=quantity2, width=width2)
            is_process = True
    except ValueError:
        print("Не корректный ввод!")
    return is_process

if __name__ == '__main__':
    while True:
        if enter_shape():
            break
    sd.pause()
