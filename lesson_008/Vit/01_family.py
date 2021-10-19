# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, money = 100, food = 50, soil = 0, eatfood = 0, workmoney = 0):
        self.money = money
        self.food = food
        self.soil = soil
        self.eatfood = eatfood
        self.workmoney = workmoney


    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
            self.food, self.money, self.soil)


class Husband:

    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.happy = 100
        self.house = None


    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}, съедено еды {}, заработано денег {}'.format(
            self.name, self.hunger, self.happy, self.house.eatfood, self.house.workmoney)

    def act(self):
        if self.house.soil >= 90:
            self.happy -= 10
        elif self.hunger < 0:
            print('{} умер из-за еды'.format(self.name))
        elif self.happy < 0:
            print('{} умер из-за депрессии'.format(self.name))
        elif self.hunger < 30:
            self.eat()
        elif self.happy < 30:
            self.gaming()
        elif self.house.money <= 60:
            self.work()

        else:
            dice_husband = randint(1, 4)
            # print('Выпало у С. ', dice_husband)
            if dice_husband == 1:
                self.eat()
            elif dice_husband == 2:
                self.work()
            elif dice_husband == 3:
                self.gaming()

    def eat(self):
        self.house.food -= 30
        self.hunger += 30
        self.house.eatfood += 30
        print('{} поел, сытости {}'.format(self.name, self.hunger))

    def work(self):
        self.hunger -= 10
        self.house.money += 150
        self.house.workmoney += 150
        print('{} сходил на работу, сытости {}'.format(self.name, self.hunger))

    def gaming(self):
        self.hunger -= 10
        self.happy += 20
        print('{} поиграл в WOT, сытости {}'.format(self.name, self.hunger))

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


class Wife:

    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.happy = 100
        self.house = None
        self.fur_count = 0

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}, количество шуб {}'.format(
            self.name, self.hunger, self.happy, self.fur_count)

    # def __str__(self):
    #     return super().__str__()

    def act(self):
        if self.house.soil >= 90:
            self.happy -= 10
        elif self.hunger < 0:
            print('{} умерла из-за еды'.format(self.name))
        elif self.happy < 0:
            print('{} умерла из-за депрессии'.format(self.name))
        elif self.hunger <= 20:
            self.eat()
        elif self.house.soil > 30:
            self.clean_house()
        else:
            dice_wife = randint(1, 5)
            # print('Выпало у М. ', dice_wife)
            if dice_wife == 1:
                self.eat()
            elif dice_wife == 2:
                self.shopping()
            elif dice_wife == 3:
                self.buy_fur_coat()
            elif dice_wife == 4:
                self.clean_house()


    def eat(self):
        self.hunger += 30
        self.house.food -= 30
        self.house.eatfood += 30
        print('{} поела, сытости {}'.format(self.name, self.hunger))

    def shopping(self):
        self.hunger -= 10
        self.house.food += 100
        self.house.money -= 100
        print('{} сходила в магазин за продуктами, сытости {}'.format(self.name, self.hunger))

    def buy_fur_coat(self):
        self.hunger -= 10
        self.house.money -= 350
        self.happy += 60
        self.fur_count += 1
        print('{} сходила в магазин за шубой, сытости {}'.format(self.name, self.hunger))

    def clean_house(self):
        self.hunger -= 10
        self.house.soil = 0

        print('{} убралась в доме {}'.format(self.name, self.hunger))

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехала в дом'.format(self.name), color='cyan')


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# serge.go_to_the_house(house=home)
# masha.go_to_the_house(house=home)
#
#
# for day in range(1, 366):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.soil += 5
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.happy = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.hunger, self.happy)
        # return super().__str__()

    def act(self):
        if self.hunger < 0:
            print('{} умерла из-за еды'.format(self.name))
        elif self.hunger <= 20:
            self.eat()
        else:
            dice_child = randint(1, 3)
            if dice_child == 1:
                self.eat()
            elif dice_child == 2:
                self.sleep()

    def eat(self):
        self.hunger += 10
        self.house.food -= 10
        self.house.eatfood += 10
        print('{} поела, сытости {}'.format(self.name, self.hunger))

    def sleep(self):
        self.hunger -= 10
        print('{} поспал, сытости {}'.format(self.name, self.hunger))

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')

serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
kolya.go_to_the_house(house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    home.soil += 5
    serge.act()
    masha.act()
    kolya.act()
    # murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    # cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

