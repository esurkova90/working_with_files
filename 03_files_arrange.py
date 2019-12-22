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


class Sorting_photo:

    def __init__(self, folder):
        self.folder = folder
        self.list_path = []

    def sorting(self):
        for dirpath, dirnames, filenames in os.walk(self.folder):
            for file in filenames:
                file_place = os.path.join(dirpath, file)
                photo_time = os.path.getmtime(file_place)
                self.file_time = time.gmtime(photo_time)
                aiming_dir = os.path.join("icons_by_year",
                                          str(self.file_time[0]), str(self.file_time[1]))
                aiming_dir_normal = os.path.normpath(aiming_dir)
                if aiming_dir_normal not in self.list_path:
                    os.makedirs(aiming_dir_normal)
                    self.list_path.append(aiming_dir_normal)
                shutil.copy2(file_place, aiming_dir_normal)


folder = "icons"
sorting_photo = Sorting_photo(folder=folder)
sorting_photo.sorting()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!
