# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

import zipfile
from pprint import pprint

class Log_parser:
    counter_per_minuts = 0
    prev_minute = 0
    time = 0
    message = 0
    num = 1

    def __init__(self, file_in):
        self.file_in = file_in
        # self.file_out = file_out
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_in, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def count(self):
        if self.file_in.endswith('.zip'):
            self.unzip()
            print('Архив найден ')
        else:
            print('Архив не найден ')
        with open(self.file_in, 'r', encoding='cp1251') as file:
            print('Файл открыт '+self.file_in)
            for line in file:
                self.time = int(line[15:17])
                self.message = line[0:17] + ']'
                object_to_find = 'NOK'
                if object_to_find in line:
                    if self.message in self.stat:
                        self.stat[self.message] += 1
                    else:
                        self.stat[self.message] = 1

    def convert_stat(self):
        file_name = 'out_counter.txt'
        file = open(file_name, mode='w')  # mode (режим): запись символьная, кодировка по умолчанию utf8
        for key, value in self.stat.items():
            print(f'{key} {value}')
            file.write(f'{key} {value}\n')
        file.close()

    def write_file(self):
        None

counter = Log_parser(file_in='events.txt')
counter.count()
counter.convert_stat()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
