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

file_events = "events.txt"
file_errors = "file_errors"


class Log_parser:

    def __init__(self, file_log, file_for_recording):
        self.file_log = file_log
        self.file_for_recording = file_for_recording
        self.file_for_writing = {}

    def append_data(self, time):
        with open(file=self.file_log, mode="r", encoding="utf-8") as file:
            for line in file:
                if "NOK" in line:
                    if time == "minute":
                        file_content = line[0:17]
                    elif time == "hour":
                        file_content = line[0:14]
                    elif time == "year":
                        file_content = line[0:5]
                    elif time == "month":
                        file_content = line[0:8]
                    if file_content in self.file_for_writing:
                        self.file_for_writing[file_content] += 1
                    else:
                        self.file_for_writing[file_content] = 1

    def recording_data(self):
        with open(file=self.file_for_recording, mode="w", encoding="utf8") as file:
            for event, count in self.file_for_writing.items():
                file.write(f"{event}] {count}\n")


log_parser = Log_parser(file_log=file_events, file_for_recording=file_errors)
log_parser.append_data(time="minute")
log_parser.recording_data()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет! 