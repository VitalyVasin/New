# -*- coding: utf-8 -*-
# Есть функция генерации списка простых чисел

def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик

class PrimeNumbers:
    def __init__(self, n):
        self.i = 1
        self.n = n
        self.number = 0
        self.prime_numbers = []
        self.iterator = iter(get_prime_numbers(n))
        self.next_element_exist = True

    def __iter__(self):
        return self

    def __next__(self):
        while self.next_element_exist:
            try:
                element_from_iterator = next(self.iterator)
                return element_from_iterator

            except UnboundLocalError:
                self.next_element_exist = False

n = 10
prime_number_iterator = PrimeNumbers(n=n)

# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield prime_numbers[-1]
    # return prime_numbers

# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def sum(dict):
    sum = 0
    for number in dict:
        sum = sum + int(number)
    return sum

def Happy_num(num):
    status = False
    l = len(str(num))
    if len(str(num)) % 2 == 0:
        if sum(str(num)[0:int(l/2)]) == sum(str(num)[((int(l/2))):l]):
            status = True

    elif len(str(num)) % 2 == 1:
        if sum(str(num)[0:int((l -1)/ 2)]) == sum(str(num)[(int((l -1)/ 2))*(-1):l]):
            status = True
    return status


def Palydrom_num(num):
    status = False
    l = len(str(num))
    dict_a = []
    dict_b = []
    if len(str(num)) % 2 == 0:
        for number in str(num)[0:int(l/2)]:
            dict_a.append(number)
        for number in str(num)[-1:((int(l/2))-1):-1]:
            dict_b.append(number)
        if dict_a == dict_b:
            status = True
    elif len(str(num)) % 2 == 1:
        for number in str(num)[0:int((l -1)/ 2)]:
            dict_a.append(number)
        for number in str(num)[-1:(int((l-1)/2)):-1]:
            dict_b.append(number)
        if dict_a == dict_b:
            status = True
    else:
        status = False

    return status


num = 123404321

# print(Happy_num(num=num))
# print(Palydrom_num(num=num))

my_numbers = [1, 101, 102, 12021, 12012, 23014]
# result_dict = filter(Happy_num, my_numbers)
# print(list(result_dict))
# result_dict = filter(Palydrom_num, my_numbers)
# print(list(result_dict))

result_dict = filter(Palydrom_num, PrimeNumbers(n=100000))
print(list(result_dict))

result_dict = filter(Happy_num, PrimeNumbers(n=100000))
print(list(result_dict))