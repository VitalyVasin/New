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

class Steam:
    def __str__(self):
        return 'Steam'

class Dirt:
    def __str__(self):
        return 'Dirt'

class Dust:
    def __str__(self):
        return 'Dust'

class Lava:
    def __str__(self):
        return 'Lava'

class Lighting:
    def __str__(self):
        return 'Lighting'

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
        mix_dict = { ('Water', '+', 'Air'): 'Storm', ('Water', '+', 'Fire'):'Steam', ('Water', '+', 'Soil'):'Dirt',
            ('Air', '+', 'Water'):'Storm', ('Air', '+', 'Fire'):'Lighting', ('Air', '+', 'Soil'):'Dust',
            ('Fire', '+', 'Water'):'Steam', ('Fire', '+', 'Air'):'Lighting', ('Fire', '+', 'Soil'):"Lava",
            ('Soil', '+', 'Water'):'Dirt', ('Soil', '+', 'Air'):'Dust', ('Soil', '+', 'Fire'):'Lava' }
        
        self.mix = 'Nothing'

        for key in mix_dict:
            goal = str(part1), '+', str(part2)
            # print('goal=', goal)
            if key == goal:
                # print(mix_dict[goal])
                self.mix = mix_dict[goal]



    def __eq__(self, other):
        return self == other

    def __str__(self):

        return self.mix

# W = Water()
# A = Air()
# F = Fire()
# S = Soil()
# result1 = F + S
# print(result1)

print(Water(), '+', Air(), '=', Water() + Air())

print(Fire(), '+', Air(), '=', Fire() + Air())



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
