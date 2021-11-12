# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import zipfile
from pprint import pprint

class Counter_char:
    common_count = 0
    num = 1

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def count(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
            print('Архив найден ')
        else:
            print('Архив не найден ')
        with open(self.file_name, 'r', encoding='cp1251') as file:
            print('Файл открыт '+self.file_name)
            for line in file:
                self._collect_for_line(line=line[:-1])
            # print('Всего букв: ', self.common_count)

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                    self.common_count +=1
                else:
                    self.stat[char] = 1
                    self.common_count +=1
            # else:
            #     None

    def convert_stat(self):
        print(f'+{"":-^9}+{"":-^10}+')
        print(f'|{"буква": ^9}|{"частота": ^10}|')
        print(f'+{"":-^9}+{"":-^10}+')
        self.pattern(number=self.num)
        # self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        for key, value in self.sorted_tuple:
            print(f'|{key: ^9}|{value: ^10}|')
        print(f'+{"":-^9}+{"":-^10}+')
        print(f'|{"итого": ^9}|{self.common_count: ^10}|')
        print(f'+{"":-^9}+{"":-^10}+')

    def pattern(self, number):
        self.number = number
        if self.number == 1:
            self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
            # Сортировка по частоте, по убыванию
        elif self.number == 2:
            self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=False)
            # Сортировка по частоте, по возрастанию
        elif self.number == 3:
            self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[0], reverse=False)
           # Сортировка по алфавиту, по возрастанию
        elif self.number == 4:
            self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[0], reverse=True)
            # Сортировка по алфавиту, по убыванию


counter = Counter_char(file_name='voyna-i-mir.txt.zip')
counter.count()
counter.convert_stat()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
