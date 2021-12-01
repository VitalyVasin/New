# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
class File_mover:
    num = 1
    path = os.path.dirname(__file__)
    path_normalized = os.path.normpath(path)
    path_jpg = os.path.join(path_normalized, 'icons')


    def __init__(self, path):
        self.path = path


    def search_file(self):
        for dirpath, dirnames, filenames in os.walk(self.path_jpg):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                # if file_time[0] == 2018:
                # print(full_file_path, secs, file_time)
                # print('year=', file_time[0], 'month=', file_time[1])
                new1 = os.path.dirname(__file__)
                src = os.path.join(dirpath, file)
                new_folder = os.path.join(new1, 'icons_by_year', str(file_time[0]), str(file_time[1]))
                dst = os.path.join(new1, 'icons_by_year', str(file_time[0]), str(file_time[1]), file)
                if os.path.isdir(new_folder):
                    print('Folder is Ok')
                else:
                    os.makedirs(new_folder)
                shutil.copy2(src=src, dst=dst)

#time.struct_time(tm_year=2018, tm_mon=2, tm_mday=27, tm_hour=13, tm_min=34, tm_sec=18, tm_wday=1, tm_yday=58, tm_isdst=0)

    def copy_file(self, src, dst):
        shutil.copy2(src=src, dst= dst)
        # print(file, src, dst)


jpg = File_mover(path=os.path.dirname(__file__))
jpg.search_file()
# jpg.copy_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
