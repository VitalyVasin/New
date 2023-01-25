# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

import multiprocessing
from os import walk


class Ticker_reader(multiprocessing.Process):
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