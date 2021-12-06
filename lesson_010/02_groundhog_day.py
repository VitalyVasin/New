# -*- coding: utf-8 -*-

# День сурка
# https://goo.gl/JnsDqu
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777

# TODO здесь ваш код
class IamGodError(Exception):
    None
class DrunkError(Exception):
    None
class CarCrashError(Exception):
    None
class GluttonyError(Exception):
    None
class DepressionError(Exception):
    None
class SuicideError(Exception):
    None

karma = 0
days = 0
class Day():
    def __init__(self, karma, days):
        self.karma = karma
        self.days = days

    def one_day(self):
        dice = randint(1, 6)
        if dice == 1:
            self.karma += dice
            self.days += 1
            raise IamGodError('')
        elif dice == 2:
            self.karma += dice
            self.days += 1
            raise DrunkError('')
        elif dice == 3:
            self.karma += dice
            self.days += 1
            raise CarCrashError('')
        elif dice == 4:
            self.karma += dice
            self.days += 1
            raise GluttonyError('')
        elif dice == 5:
            self.karma += dice
            self.days += 1
            raise DepressionError('')
        elif dice == 6:
            self.karma += dice
            self.days += 1
            raise SuicideError('')
        else:
            print('111')
    # return karma
Day1 = Day(karma=karma, days=days)
while Day1.karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:

        Day1.one_day()

    except IamGodError:
        print('Сегодня вылетело IamGodError')
    except DrunkError:
        print('Сегодня вылетело DrunkError')
    except CarCrashError:
        print('Сегодня вылетело CarCrashError')
    except GluttonyError:
        print('Сегодня вылетело GluttonyError')
    except DepressionError:
        print('Сегодня вылетело DepressionError')
    except SuicideError:
        print('Сегодня вылетело SuicideError')

print('Days = ', Day1.days)