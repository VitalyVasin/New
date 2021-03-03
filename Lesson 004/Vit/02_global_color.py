# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

length = 200
angle = 0
width = 5
point_trangle = sd.get_point(50, 380)
point_square = sd.get_point(350, 380)
point_5corner = sd.get_point(100, 50)
point_6corner = sd.get_point(400, 50)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)


def enter_color():
    input_text = input ("0 : RED, \n1 : ORANGE, \n2 : YELLOW, \n3 : GREEN, \n4 : CYAN, \n5 : BLUE, \n6 : PURPLE \nВведите номер требуемого цвета: ")
    try:
        test_number = int(input_text)
        print("Это правильный ввод! Ваше счастливое число: ", test_number)
        if test_number == 0:
            drawing(color=COLOR_RED)
        elif test_number == 1:
            drawing(color=COLOR_ORANGE)
        elif test_number == 2:
            drawing(color=COLOR_YELLOW)
        elif test_number == 3:
            drawing(color=COLOR_GREEN)
        elif test_number == 4:
            drawing(color=COLOR_CYAN)
        elif test_number == 5:
            drawing(color=COLOR_BLUE)
        elif test_number == 6:
            drawing(color=COLOR_PURPLE)
        else:
            print("Не корректный ввод!")
            enter_color()
    except ValueError:
        print("Не корректный ввод!")
        enter_color()
    return

def drawing(color):
    # enter_color()
    triangle(point=point_trangle, length=length, angle=angle, color=color, width=width)
    square(point=point_square, length=length, angle=angle, color=color, width=width)
    fivecorner(point=point_5corner, length=length, angle=angle, color=color, width=width)
    sixcorner(point=point_6corner, length=length, angle=angle, color=color, width=width)
    return color

def triangle(point, length, angle, color, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=width)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=width)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=width)
    v3.draw(color=color)

def square(point, length, angle, color, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=width)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=200, width=width)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=200, width=width)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=200, width=width)
    v4.draw(color=color)

def fivecorner(point, length, angle, color, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=130, width=width)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=130, width=width)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=130, width=width)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=130, width=width)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=130, width=width)
    v5.draw(color=color)

def sixcorner(point, length, angle, color, width):
    v1 = sd.get_vector(start_point=point, angle=angle, length=120, width=width)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=120, width=width)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=120, width=width)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=120, width=width)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=120, width=width)
    v5.draw(color=color)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=120, width=width)
    v6.draw(color=color)


enter_color()

sd.pause()
