# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

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
        file.close()
        for group_time, event_count in self.stat.items():
            yield group_time, event_count

grouped_events = Log_parser(file_in='events.txt')

for group_time, event_count in grouped_events.count():
    print(f'[{group_time}] {event_count}')
