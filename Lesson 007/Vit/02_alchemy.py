# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

result_part = 1
class Storm:
    def __str__(self):
        return 'Storm'

class Water:

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        return Mixer(part1=self, part2=other)


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        return Mixer(part1=self, part2=other)

class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        return Mixer(part1=self, part2=other)

class Soil:
    def __str__(self):
        return 'Soil'

    def __add__(self, other):
        return Mixer(part1=self, part2=other)



class Mixer:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
        self.mix = 'Nothing'
        if str(self.part1) == 'Water':
            if str(self.part2) == 'Air':
                self.mix = 'Storm'
            elif str(self.part2) == 'Fire':
                self.mix = 'Steam'
            elif str(self.part2) == 'Soil':
                self.mix = 'Dirt'
            else:
                self.mix = 'None'
        elif str(self.part1) == 'Air':
            if str(self.part2) == 'Water':
                self.mix = 'Storm'
            elif str(self.part2) == 'Fire':
                self.mix = 'Lighting'
            elif str(self.part2) == 'Soil':
                self.mix = 'Dust'
            else:
                self.mix = 'None'
        elif str(self.part1) == 'Fire':
            if str(self.part2) == 'Water':
                self.mix = 'Steam'
            elif str(self.part2) == 'Air':
                self.mix = 'Lighting'
            elif str(self.part2) == 'Soil':
                self.mix = 'Lava'
            else:
                self.mix = 'None'
        elif str(self.part1) == 'Soil':
            if str(self.part2) == 'Water':
                self.mix = 'Dirt'
            elif str(self.part2) == 'Air':
                self.mix = 'Dust'
            elif str(self.part2) == 'Fire':
                self.mix = 'Lava'
            else:
                self.mix = 'None'

        else:
            self.mix = '= None'

    def __eq__(self, other):
        return self == other

    def __str__(self):

        return self.mix

W = Water()
A = Air()
F = Fire()
S = Soil()
# result1 = F + S
# print(result1)

print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

print(Water()+Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
