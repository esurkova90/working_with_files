# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import re

wrong_data = []
true_data = []


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def name_exeptions(name):
    wrong_names = re.findall('(\d+)', name)
    for wrong_name in wrong_names:
        if wrong_name in name:
            raise NotNameError


def email_exeptios(mail):
    if "@" not in mail or "." not in mail:
        raise NotEmailError


def age_exeptions(age):
    age = int(age)
    if age < 10 or age > 99:
        raise ValueError


def collecting_data(line):
    try:
        name, mail, age = line.split(' ')
        try:
            name_exeptions(name=name)
        except NotNameError:
            wrong_data.append(line)
        try:
            email_exeptios(mail=mail)
        except NotEmailError:
            wrong_data.append(line)
        try:
            age_exeptions(age=age)
        except ValueError:
            wrong_data.append(line)
    except ValueError:
        wrong_data.append(line)


with open(file="registrations.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        collecting_data(line=line)
        if line not in wrong_data:
            true_data.append(line)

with open(file="registrations_bad.log", mode="w", encoding="utf-8") as file:
    for bad_data in wrong_data:
        file.write(f"{bad_data}")

with open(file="registrations_good.log", mode="w", encoding="utf-8") as file:
    for good_data in true_data:
        file.write(f"{good_data}")

# зачет!
