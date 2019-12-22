# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


def make_ticket(fio, from_, to, date, save_to):
    im = Image.open("images/ticket_template.png")
    draw = ImageDraw.Draw(im)
    font_path = os.path.normpath("python_snippets/fonts/ofont.ru_Graphite Std.ttf")
    font = ImageFont.truetype(font=font_path, size=18)

    y = im.size[1] - 220 - (10 + font.size) * 2
    draw.text((50, y), fio, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 150 - (10 + font.size) * 2
    draw.text((50, y), from_, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 85 - (10 + font.size) * 2
    draw.text((50, y), to, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 85 - (10 + font.size) * 2
    draw.text((290, y), date, font=font, fill=ImageColor.colormap['black'])

    im.show()
    save_to = save_to if save_to else 'probe.png'
    im.save(save_to)


make_ticket(fio="Иванов И.И.", from_="Moscow", to="Paris", date="Now!", save_to="probe.png")

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
parser = argparse.ArgumentParser()
parser.add_argument("fio")
parser.add_argument("from_", type=str)
parser.add_argument("to", type=str)
parser.add_argument("date", type=str)
parser.add_argument("-save_to", type=str)
args = parser.parse_args()
make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_to=args.save_to)
# зачет!