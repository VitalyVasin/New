#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Dima')
my_family.append('Olga')
my_family.append('Alexander')

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Dima', 183],
]
my_family_height.append(['Olga', 174])
my_family_height.append(['Alexander', 187])

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца ' + str(my_family_height[2][1]) + ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_rost = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи - ' + str(sum_rost) + ' см')