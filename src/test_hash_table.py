import random
from modules.hash_table import HashTable
import matplotlib.pyplot as plt
import time
from modules.commands import Commands


def average_value(y, x):
    n = 10
    for i in range(int(len(y) / n)):
        cur = 0
        for j in range(n):
            cur += y[i * n + j]
        cur = cur / n
        for j in range(n):
            if y[i * n + j] > cur:
                y[i * n + j] = cur
    return y, x


class TestHashTable:
    def __init__(self, kol, command):
        self.kol = kol
        self.command = command

    def start(self):
        arr = list(range(self.kol))
        random.shuffle(arr)
        h = HashTable()

        plt.xlabel('Количество элементов')
        plt.ylabel('Время')
        plt.grid()
        y = []
        x = []
        if self.command == Commands.INSERT:
            plt.title("Вставка")
            for i in range(self.kol):
                t = time.perf_counter()
                h.insert(i, i)
                y.append(time.perf_counter() - t)
                x.append(i)
            y, x = average_value(y, x)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        for i in range(self.kol):
            h.insert(arr[i], i)

        if self.command == Commands.FIND:
            plt.title("Поиск")
            random.shuffle(arr)
            for i in range(self.kol):
                t = time.perf_counter()
                h.find(arr[i])
                y.append(time.perf_counter() - t)
                x.append(i)
            #y, x = average_value(y, x)
            plt.scatter(x, y, s=5)
            plt.show()
            return

        if self.command == Commands.REMOVE:
            plt.title("Удаление")
            random.shuffle(arr)
            for i in range(self.kol):
                t = time.perf_counter()
                h.remove(i)
                y.append(time.perf_counter() - t)
                x.append(i)
            y, x = average_value(y, x)
            plt.scatter(x, y, s=5)
            plt.show()
            return

