# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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
import os

from collections import OrderedDict, defaultdict
import threading


class Volatility(threading.Thread):

    def __init__(self, file, volatilities, lock):
        super(Volatility, self).__init__()
        self.file = file
        self.lock = lock
        self.volatilities = volatilities

    def run(self):
        prices = []
        with open(file=self.file, mode="r") as file:
            for line in file:
                ticker, time, price, quantity = line.split(',')
                if price == "PRICE":
                    pass
                else:
                    real_price = float(price)
                    prices.append(real_price)
            max_price = (max(prices))
            min_price = (min(prices))
            average_price = (max_price + min_price) / 2
            volotility = ((max_price - min_price) / average_price) * 0.1
            with self.lock:
                self.volatilities[ticker] = volotility


class VoloManager():
    def __init__(self):
        self.all_files = []
        self.volatilities = defaultdict(int)
        self.zero_volotilities = {}
        self.max_min_volotilities = {}

    def run(self):
        for dirpath, dirnames, filenames in os.walk(dirs):
            for file in filenames:
                full_file = os.path.join(dirs, file)
                self.all_files.append(full_file)

    def find_zero_volotility(self):
        lock = threading.Lock()
        self.instances = [Volatility(file=file, volatilities=self.volatilities, lock=lock) for file in self.all_files]
        for instance in self.instances:
            instance.start()
        for instance in self.instances:
            instance.join()
            for ticker, volotility in instance.volatilities.items():
                if volotility == 0.0:
                    self.zero_volotilities[ticker] = volotility
                else:
                    self.max_min_volotilities[ticker] = volotility

    def find_min_volotility(self):
        self.min_volotilities = OrderedDict(
            sorted(self.max_min_volotilities.items(), key=lambda x: x[1], reverse=False))
        self.min_volotilities = list(self.min_volotilities.items())
        return self.min_volotilities[:4]

    def find_max_volotility(self):
        self.max_volotilities = OrderedDict(
            sorted(self.max_min_volotilities.items(), key=lambda x: x[1], reverse=True))
        self.max_volotilities = list(self.max_volotilities.items())
        return self.max_volotilities[:4]

    def output_zero(self):
        self.zero_volotilities = OrderedDict(sorted(self.zero_volotilities.items(), key=lambda x: x[0], reverse=False))
        zero_tickers = list(self.zero_volotilities)
        print(*zero_tickers, sep=', ')

    def output_max_min(self, volo):
        volo = (sorted(volo, reverse=True))
        for max_min_data in volo:
            print(f"{max_min_data[0]} - {max_min_data[1]}%")

    def show_result(self):
        self.find_zero_volotility()
        min_volo = self.find_min_volotility()
        max_volo = self.find_max_volotility()
        print("Максимальная волотильность:")
        self.output_max_min(volo=max_volo)
        print("Минимальная волотильность:")
        self.output_max_min(volo=min_volo)
        print("Нулевая волотильность:")
        self.output_zero()


dirs = "trades"

volo_manager = VoloManager()
volo_manager.run()
volo_manager.show_result()
