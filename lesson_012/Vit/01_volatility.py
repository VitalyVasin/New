# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле

import os
import operator
from os import walk


class Ticker_reader:
    # TRADETIME = 0
    # SECID = 0
    # PRICE = 0
    # QUANTITY = 0
    # price_list = []
    volatility_dict = {}

    def __init__(self, file_in):
        self.file_in = file_in
        self.stat = {}
        self.TRADETIME = 0
        self.SECID = 0
        self.PRICE = 0
        self.QUANTITY = 0
        self.price_list = []
        # self.volatility_dict = {}

    def run(self):
        pass

    def count(self):
        with open(self.file_in, 'r', encoding='cp1251') as file:
            self.price_list = []
            for line in file:
                if (line.split(",")[0:-3])[-1] == 'SECID':
                    pass
                else:
                    self.SECID = (line.split(",")[0:-3])[-1]
                if (line.split(",")[1:-2])[-1] == 'TRADETIME':
                    pass
                else:
                    self.TRADETIME = (line.split(",")[1:-2])[-1]

                if (line.split(",")[2:-1])[-1] == 'PRICE':
                    pass
                else:
                    self.PRICE = float((line.split(",")[2:-1])[-1])
                    self.price_list.append(self.PRICE)
                if (line.split(",")[1:4])[-1] == 'QUANTITY':
                    pass
                else:
                    self.QUANTITY  = (line.split(",")[1:4])[-1]

            self.price_list.sort()
            min_price = self.price_list[0]
            max_price = self.price_list[-1]
            average_price = (max_price + min_price) / 2
            self.volatility_dict[self.SECID] = ((max_price - min_price) / average_price) * 100

def main():
    f = []
    for (dirpath, dirnames, filenames) in walk('trades'):
        f.extend(filenames)
        break
    for file in f:
        full_filename = "trades/" + file

        counter = Ticker_reader(file_in=full_filename)
        counter.count()

    sorted_tuples = sorted(counter.volatility_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples}

    zero_volatility = {}
    final_volatility_dict = {}

    for key, val in sorted_dict.items():
        if val == 0.0:
            zero_volatility[key] = val
        else:
            final_volatility_dict[key] = val

    sorted_final_volatility_dict = sorted(final_volatility_dict.items(), key=lambda item: item[1])
    sorted_final_volatility_dict = dict(sorted_final_volatility_dict)

    sorted_zero_volatility = sorted(zero_volatility.items(), key=lambda item: item[0])
    sorted_zero_volatility = dict(sorted_zero_volatility)

    print('Минимальная волатильность:')
    for name, value in {i: sorted_final_volatility_dict[i] for i in list(sorted_final_volatility_dict)[:3]}.items():
        print(name, ' - ', round(value, 2), '%')

    print('Максимальная волатильность:')
    for name, value in {i: sorted_final_volatility_dict[i] for i in list(sorted_final_volatility_dict)[-3:]}.items():
        print(name, ' - ', round(value, 2), '%')

    zero_volatility_result = []
    for name, value in sorted_zero_volatility.items():
        zero_volatility_result.append(name)
    print('Нулевая волатильность:')
    print(*zero_volatility_result, sep=", ")


if __name__ == '__main__':
    main()